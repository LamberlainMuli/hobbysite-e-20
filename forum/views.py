from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic import TemplateView
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import ThreadForm, ThreadUpdateForm, CommentForm

from .models import Thread, ThreadCategory, Comment


class ThreadListView(ListView):
    model = ThreadCategory
    template_name = 'forum/forum_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
          
        categories = ThreadCategory.objects.all()
        threads_per_category = {}
        for category in categories:
            category_threads = Thread.objects.filter(category=category).exclude(author=self.request.user)
            threads_per_category[category] = category_threads
        context['threads_per_category'] = threads_per_category
        context['my_threads'] = Thread.objects.filter(author=self.request.user)
        context['all_threads'] = Thread.objects.exclude(author=self.request.user)
        context['category'] = categories

        return context


class ThreadDetailView(DetailView):
    model = Thread
    template_name = 'forum/forum_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        threads = Thread.objects.all()
        categories = ThreadCategory.objects.all()
        context['categories'] = categories
        
        return context

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        thread = self.get_object()
        category_threads = Thread.objects.filter(category=thread.category).exclude(pk=thread.pk)
        context['category_threads'] = category_threads
        context['comment_form'] = CommentForm()
        context['comment'] = Comment.objects.filter(thread=thread).order_by('created_on')
        
        if self.request.user == thread.author:
            context['is_owner'] = True
        else:
            context['is_owner'] = False
        
        return context
    
    def post(self, request, *args, **kwargs):
        thread = self.get_object()
        form = CommentForm(request.POST)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.thread = thread
            comment.author = request.user
            comment.save()
            return self.get(request, *args, **kwargs)
        else:
            return self.render_to_response(self.get_context_data(form=form))


class ForumIndex(ListView):
    model = Thread
    template_name = 'forum/index.html'
    context_object_name = 'post_list'
    paginate_by = 5

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        posts = Thread.objects.all().order_by('-created_on')
        categories = ThreadCategory.objects.all()
        context['categories'] = categories
        context['recent_posts'] = posts[:5]
        context['latest_post'] = posts.first() if posts.exists() else None
        context['total_posts'] = posts.count()
        context['total_words'] = sum([post.get_word_count() for post in posts])
        context['average_read_time'] = sum([post.get_read_time() for post in posts]) / context['total_posts'] if context['total_posts'] > 0 else 0
        return context

    

class ThreadCreateView(LoginRequiredMixin, CreateView):
    model = Thread
    template_name = "forum/forum_create.html"
    form_class = ThreadForm

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class ThreadUpdateView(LoginRequiredMixin, UpdateView):
    model = Thread
    template_name = "forum/forum_update.html"
    form_class = ThreadUpdateForm

    def get_success_url(self):
        return reverse_lazy(
            "forum:forum_update", kwargs={"pk": self.object.thread.pk}
        )

    def form_valid(self, form):
        form.instance.thread = Thread.objects.get(pk=self.kwargs["pk"])
        return super().form_valid(form)