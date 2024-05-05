from django.urls import path
from .views import ArticleDetailView, ArticleListView, BlogIndex


urlpatterns = [
    path('articles', ArticleListView.as_view(), name='article_list'),
    path('articles/<int:pk>', ArticleDetailView.as_view(), name='article_detail'),
    path("article/add", ArticleCreateView.as_view(), name="article_create"),
    path("article/<int:pk>/edit", ArticleUpdateView.as_view(), name="article_update"),
    path('', BlogIndex.as_view(), name='index'),
]


app_name = 'blog'