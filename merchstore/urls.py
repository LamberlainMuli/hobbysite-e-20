from django.urls import path

from .views import ProductListView, ProductDetailView, ProductCreateView, ProductUpdateView, CartView, TransactionListView, ProductIndex


urlpatterns = [
    path("items", ProductListView.as_view(), name="merch_list"),
    path("item/<int:pk>", ProductDetailView.as_view(), name="merch_detail"),
    path("item/add", ProductCreateView.as_view(), name="merch_create"),
    path("item/<int:pk>/edit", ProductUpdateView.as_view(), name="merch_update"),
    path("cart", CartView.as_view(), name="cart"),
    path("transactions", TransactionListView.as_view(), name="transaction_list"),
    path('', ProductIndex.as_view(), name = 'index'),
]

app_name = "merchstore"