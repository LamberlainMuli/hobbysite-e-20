from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from .models import Article,ArticleCategory


class WikiListView(ListView):
    model = ArticleCategory
    template_name = 'wiki/wiki_list.html'


class WikiDetailView(DetailView):
    model = Article
    template_name = 'wiki/wiki_detail.html'




