from django.urls import path
from .views import ProductListView, ProductDetailView, ProductIndex

urlpatterns = [
    path('items', ProductListView.as_view(), name = 'merch_list'),
    path('item/<int:pk>', ProductDetailView.as_view(), name = 'merch_detail'),
    path('', ProductIndex.as_view(), name = 'index'),
]

app_name = "merchstore"