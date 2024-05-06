from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Commission, Job, JobApplication
from .forms import CommissionForm, CommissionUpdateForm, JobCreateForm, JobApplicationForm

class CommissionListView(LoginRequiredMixin, ListView):
    model = Commission
    template_name = 'commissions/commission_list.html'

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.order_by('-status', '-created_on')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user_commissions'] = Commission.objects.filter(creator=self.request.user)
        context['applied_commissions'] = Commission.objects.filter(jobs__applications__applicant=self.request.user.profile)
        return context

class CommissionDetailView(LoginRequiredMixin, DetailView):
    model = Commission
    template_name = 'commissions/commission_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        commission = self.get_object()
        context['jobs'] = Job.objects.filter(commission=commission)
        context['total_manpower_required'] = sum(job.manpower_required for job in context['jobs'])
        context['total_open_manpower'] = sum(job.manpower_required - JobApplication.objects.filter(job=job, status='Accepted').count() for job in context['jobs'])
        context['can_edit'] = self.request.user == commission.creator
        context['job_application_form'] = JobApplicationForm()
        return context

    def post(self, request, *args, **kwargs):
        job_application_form = JobApplicationForm(request.POST)
        if job_application_form.is_valid():
            job_application = job_application_form.save(commit=False)
            job_application.applicant = request.user.profile
            job_application.job = self.get_object()
            job_application.save()
            return self.get(request, *args, **kwargs)
        else:
            return self.render_to_response(self.get_context_data(job_application_form=job_application_form))

class CommissionCreateView(LoginRequiredMixin, CreateView):
    model = Commission
    form_class = CommissionForm
    template_name = 'commissions/commission_create.html'

    def form_valid(self, form):
        form.instance.creator = self.request.user
        return super().form_valid(form)

class CommissionUpdateView(LoginRequiredMixin, UpdateView):
    model = Commission
    form_class = CommissionUpdateForm
    template_name = 'commissions/commission_update.html'

    def form_valid(self, form):
        commission = form.save(commit=False)
        if all(job.status == 'Full' for job in commission.jobs.all()):
            commission.status = 'Full'
        commission.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('commissions:commission-detail', kwargs={'pk': self.object.pk})


class CommissionIndex(ListView):
    model = Commission
    template_name = 'commissions/index.html'
    context_object_name = 'commissions_list'
    paginate_by = 5

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        commissions = Commission.objects.all()
        context['recent_commissions'] = commissions[:5]
        context['latest_commission'] = commissions.first()
        context['total_commissions'] = commissions.count()
        context['total_words'] = sum(commission.get_word_count() for commission in commissions)
        context['total_read_time'] = context['total_words']/200
        context['average_read_time'] = sum(commission.get_read_time() for commission in commissions) / context['total_commissions'] if context['total_commissions'] > 0 else 0
        return context