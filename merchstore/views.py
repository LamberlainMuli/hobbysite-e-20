from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from .models import Product, ProductType

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
    paginate_by = 5

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        products = Product.objects.all()
        types = ProductType.objects.all()
        context['types'] = types
        context['recent_products'] = products[:5]
        context['latest_product'] = products.first()
        context['total_products'] = products.count()
        context['total_words'] = sum(product.get_word_count() for product in products)
        context['total_read_time'] = context['total_words']/200
        context['average_read_time'] = sum(product.get_read_time() for product in products) / context['total_products'] if context['total_products'] > 0 else 0
        return context