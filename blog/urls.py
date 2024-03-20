from django.urls import path
from .views import ArticleDetailView, ArticleListView


urlpatterns = [
    path('blog/articles', ArticleListView.as_view(), name='article_list'),
    path('blog/articles/<int:pk>', ArticleDetailView.as_view(), name='article_detail'),
]


app_name = 'blog'