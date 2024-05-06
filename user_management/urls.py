from django.urls import path
from .views import ProfileUpdateView

app_name = 'user_management'

urlpatterns = [
    path('', ProfileUpdateView.as_view(), name='profile_update'),
]

app_name = 'user_management'