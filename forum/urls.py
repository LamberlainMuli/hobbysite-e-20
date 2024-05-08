from django.urls import path

from .views import ThreadListView, ThreadDetailView, ThreadCreateView, ThreadUpdateView, ForumIndex

urlpatterns = [
    path('threads', ThreadListView.as_view(), name='forum_list'),
    path('thread/<int:pk>', ThreadDetailView.as_view(), name='forum_detail'),
    path('thread/add', ThreadCreateView.as_view(), name='forum_create'),
    path('thread/<int:pk>/edit', ThreadUpdateView.as_view(), name='forum_update'),
    path('', ForumIndex.as_view(), name='index'),   
]

app_name = 'forum'