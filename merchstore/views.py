from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from .models import Product

class ProductListView(ListView):
    model = Product
    template_name = 'merchstore/product_list.html'

class ProductDetailView(DetailView):
    model = Product
    template_name = 'merchstore/product_detail.html'
    
class ProductIndex(ListView):
    model = Product
    template_name = 'merchstore/index.html'
    context_object_name = 'product_list'
    paginate_by = 2
    