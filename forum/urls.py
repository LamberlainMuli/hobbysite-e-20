from django.urls import path

from .views import ForumListView, ForumDetailView, ForumIndex

urlpatterns = [
    path('threads', ForumListView.as_view(), name='forum_list'),
    path('thread/<int:pk>', ForumDetailView.as_view(), name='forum_detail'),
    path('', ForumIndex.as_view(), name='index'),   
]

app_name = 'forum'