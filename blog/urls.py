from django.urls import path
from .views import ArticleDetailView, ArticleListView, BlogIndex


urlpatterns = [
    path('articles', ArticleListView.as_view(), name='article_list'),
    path('articles/<int:pk>', ArticleDetailView.as_view(), name='article_detail'),
    path('', BlogIndex.as_view(), name='index'),
]


app_name = 'blog'