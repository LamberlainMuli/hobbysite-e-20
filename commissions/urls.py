# <appname>/urls.py
from django.urls import path
from .views import CommissionDetailView, CommissionListView
from .views import (
    CommissionListView, 
    CommissionDetailView, 
    CommissionCreateView, 
    CommissionUpdateView
)

urlpatterns = [
    path("list", CommissionListView.as_view(), name="commission_list"),
    path("<int:pk>", CommissionDetailView.as_view(), name="commission-detail"),
    path("add/", CommissionCreateView.as_view(), name="commission-create"),
    path("<int:pk>/edit", CommissionUpdateView.as_view(), name="commission-update"),
    path("", CommissionIndex.as_view(), name="index")
]

app_name = "commissions"  