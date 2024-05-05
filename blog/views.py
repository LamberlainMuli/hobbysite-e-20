from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic import TemplateView
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView
from .forms import ArticleForm, ArticleUpdateForm
from .models import Article, ArticleCategory
from django.contrib.auth.mixins import LoginRequiredMixin


class ArticleListView(ListView):
    model = ArticleCategory
    template_name = 'blog/article_list.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
          
        categories = ArticleCategory.objects.all()
        articles_per_category = {}
        for category in categories:
          category_articles = Article.objects.filter(category=category).exclude(author=self.request.user.profile)
          articles_per_category[category] = category_articles
        context['articles_per_category'] = articles_per_category
        context['my_articles'] = Article.objects.filter(author=self.request.user.profile)
        context['all_article'] = Article.objects.exclude(author=self.request.user.profile)
        context['category'] = categories
    
        return context
    

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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        article = self.get_object()
        author_articles = Article.objects.filter(author=article.author).exclude(pk=article.pk)
        context['author_articles'] = author_articles
        return context


class ArticleCreateView(LoginRequiredMixin, CreateView):
    model = Article
    template_name = "blog/article_create.html"
    form_class = ArticleForm

    def form_valid(self, form):
        form.instance.author = self.request.user.profile
        return super().form_valid(form)


class ArticleUpdateView(LoginRequiredMixin, UpdateView):
    model = Article
    template_name = "blog/article_update.html"
    form_class = ArticleUpdateForm

    def get_success_url(self):
        return reverse_lazy(
            "blog:article_update", kwargs={"pk": self.object.article.pk}
        )

    def form_valid(self, form):
        form.instance.article = Article.objects.get(pk=self.kwargs["pk"])
        return super().form_valid(form)
    
