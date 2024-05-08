from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from .models import Article,ArticleCategory,Comment
from .forms import WikiForm,WikiEditForm,WikiTitleFilterForm,CommentForm

from django.views.generic.edit import CreateView, UpdateView
from django.urls import reverse_lazy

class WikiListView(ListView):
    model = ArticleCategory
    template_name = 'wiki/wiki_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Get all categories
        categories = ArticleCategory.objects.all()
        # Create a dictionary to store articles per category
        articles_per_category = {}
        # Check if the user is authenticated
        if self.request.user.is_authenticated:
            for category in categories:
                # Filter articles for the current category
                category_articles = Article.objects.filter(category=category).exclude(author=self.request.user.profile)
                # Add the filtered articles to the dictionary with category as key
                articles_per_category[category] = category_articles
            # Add the articles per category dictionary to the context
            context['articles_per_category'] = articles_per_category
            context['my_articles'] = Article.objects.filter(author=self.request.user.profile)
            context['all_article'] = Article.objects.exclude(author=self.request.user.profile)
            context['category'] = categories
        else:
            # If the user is not authenticated, show all articles
            context['all_articles'] = Article.objects.all()
            context['my_articles'] = Article.objects.all()

        return context
    
class WikiDetailView(DetailView):
    model = Article
    template_name = 'wiki/wiki_detail.html'
    
    def get_context_data(self, **kwargs):
     context = super().get_context_data(**kwargs)
     article = self.get_object()

        # Filter articles by categories instead of authors
     category_articles = Article.objects.filter(category=article.category).exclude(pk=article.pk)[:2]

     context['category_articles'] = category_articles
     context['comment_form'] = CommentForm()
     context['comments'] = Comment.objects.filter(article=article).order_by('-created_on')

     return context

    def post(self, request, *args, **kwargs):
        article = self.get_object()
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.article = article
            comment.author = request.user.profile  # Assuming user is logged in
            comment.save()
            return self.get(request, *args, **kwargs)  # Refresh the page
        else:
            return self.render_to_response(self.get_context_data(form=form))

class WikiCreateView(LoginRequiredMixin, CreateView):
    model = Article
    template_name = "wiki/wiki_create.html"
    form_class = WikiForm

    def form_valid(self, form):
        form.instance.author = self.request.user.profile
        return super().form_valid(form)

class WikiUpdateView(LoginRequiredMixin, UpdateView):
    model = Article
    template_name= "wiki/wiki_update.html"
    queryset = Article.objects.all()
    form_class = WikiEditForm

    def get_context_data(self, **kwargs):
        context = super(WikiUpdateView, self).get_context_data(**kwargs)
        context['pk'] = Article.objects.filter(pk=self.kwargs.get('pk'))
        return context
    
    def form_valid(self, form):
        form.instance.author = self.request.user.profile
        return super().form_valid(form)


def index(request):
    title = request.GET.get('title')
    context = {
        'forms': WikiTitleFilterForm(),
        'articles': Article.objects.all()
    }
    return render(request,'wiki/wiki_list.html',context)

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
