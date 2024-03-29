from django.urls import path
from .views import ProductListView, ProductDetailView

urlpatterns = [
    path('items', ProductListView.as_view(), name = 'merch_list'),
    path('item/<int:pk>', ProductDetailView.as_view(), name = 'merch_detail')
]

app_name = "merchstore"