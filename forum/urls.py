from django.urls import path

from .views import ForumListView, ForumDetailView

urlpatterns = [
    path('threads', ForumListView.as_view(), name='forum_list'),
    path('thread/<int:pk>', ForumDetailView.as_view(), name='forum_detail'),
]

app_name = 'forum'