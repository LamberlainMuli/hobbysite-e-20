from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from .models import Article,ArticleCategory


class WikiListView(ListView):
    model = ArticleCategory
    template_name = 'wiki/wiki_list.html'


class WikiDetailView(DetailView):
    model = Article
    template_name = 'wiki/wiki_detail.html'

class WikiIndex(ListView):
    model = Article
    template_name = 'wiki/index.html'
    context_object_name = 'article_list'
    paginate_by = 5

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        articles = Article.objects.all().order_by('-created_on')
        categories = ArticleCategory.objects.all()
        context['categories'] = categories
        context['recent_articles'] = articles[:5]
        context['latest_article'] = articles.first() if articles.exists() else None
        context['total_articles'] = articles.count()
        context['total_words'] = sum([article.get_word_count() for article in articles])
        context['average_read_time'] = sum([article.get_read_time() for article in articles]) / context['total_articles'] if context['total_articles'] > 0 else 0
        return context
