from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Commission, Job, JobApplication
from .forms import CommissionForm, CommissionUpdateForm, JobCreateForm, JobApplicationForm
from django.db.models import Case, When

class CommissionListView(LoginRequiredMixin, ListView):
    model = Commission
    template_name = 'commissions/commission_list.html'

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.order_by(
            Case(When(status='Open', then=0),
                 When(status='Full', then=1),
                 When(status='Completed', then=2),
                 When(status='Discontinued', then=3),
                 default=4
                 ), 
            '-created_on')


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user_commissions'] = Commission.objects.filter(creator=self.request.user)
        context['applied_commissions'] = Commission.objects.filter(jobs__applications__applicant=self.request.user)
        return context

class CommissionDetailView(LoginRequiredMixin, DetailView):
    model = Commission
    form_class = JobApplicationForm
    template_name = 'commissions/commission_detail.html'
    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        commission = self.get_object()

        context['jobs'] = commission.jobs.all()
        context['can_edit'] = self.request.user == commission.creator
        jobs = context['jobs']  
        context['total_manpower_required'] = sum(job.manpower_required for job in jobs)
        
        return context

    def form_valid(self, form):
        application = form.save(commit=False)
        application.applicant = self.request.user
        application.job = self.get_object()
        application.status = 'Pending'
        application.save()
        return super().form_valid(form)

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