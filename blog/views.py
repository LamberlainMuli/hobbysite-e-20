from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic import TemplateView
from .models import Article, ArticleCategory


class ArticleListView(ListView):
    model = ArticleCategory
    template_name = 'blog/article_list.html'


class ArticleDetailView(DetailView):
    model = Article
    template_name = 'blog/article_detail.html'
    
class BlogIndex(ListView):
    model = Article
    template_name = 'blog/index.html'
    context_object_name = 'article_list'
    paginate_by = 5

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        articles = Article.objects.all()
        categories = ArticleCategory.objects.all()
        context['categories'] = categories
        context['recent_articles'] = articles[:5]
        context['latest_article'] = articles.first()
        context['total_articles'] = articles.count()
        context['total_words'] = sum(article.entry.count(' ')+1 for article in articles)
        context['total_read_time'] = context['total_words']/200
        context['average_read_time'] = sum((article.entry.count(' ')+1)/200 for article in articles) / context['total_articles'] if context['total_articles'] > 0 else 0
        return context