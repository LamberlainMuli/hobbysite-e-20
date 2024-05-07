# <appname>/urls.py
from django.urls import path
from .views import CommissionDetailView, CommissionListView, CommissionIndex

urlpatterns = [
    path("list", CommissionListView.as_view(), name="commission_list"),
    path("<int:pk>", CommissionDetailView.as_view(), name="commission-detail"),
    path("", CommissionIndex.as_view(), name="index")
]

app_name = "ledger"