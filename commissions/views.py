from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Commission

class CommissionListView(ListView):
    model = Commission
    template_name = 'commissions/commission_list.html'

class CommissionDetailView(DetailView):
    model = Commission
    template_name = 'commissions/commission_detail.html'

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