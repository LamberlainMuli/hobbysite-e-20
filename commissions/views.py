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
    context_object_name = 'commission_list'
    paginate_by = 2