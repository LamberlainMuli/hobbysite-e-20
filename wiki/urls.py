from django.urls import path

from .views import WikiListView, WikiDetailView, WikiIndex

urlpatterns = [
    path('articles', WikiListView.as_view(), name="wiki_list"), 
    path('article/<int:pk>', WikiDetailView.as_view(), name = "wiki_detail"),
    path('', WikiIndex.as_view(), name="index"),
    ]

app_name = "wiki"

