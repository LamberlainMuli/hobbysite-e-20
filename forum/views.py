from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Post, PostCategory


class ForumListView(ListView):
    model = PostCategory
    template_name = 'forum/forum_list.html'


class ForumDetailView(DetailView):
    model = Post
    template_name = 'forum/forum_detail.html'


class ForumIndex(ListView):
    model = Post
    template_name = 'forum/index.html'
    context_object_name = 'post_list'
    paginate_by = 5

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        posts = Post.objects.all().order_by('-created_on')
        categories = PostCategory.objects.all()
        context['categories'] = categories
        context['recent_posts'] = posts[:5]
        context['latest_post'] = posts.first() if posts.exists() else None
        context['total_posts'] = posts.count()
        context['total_words'] = sum([post.get_word_count() for post in posts])
        context['average_read_time'] = sum([post.get_read_time() for post in posts]) / context['total_posts'] if context['total_posts'] > 0 else 0
        return context
