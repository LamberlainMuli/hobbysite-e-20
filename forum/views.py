from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from .models import Post, PostCategory


class ForumListView(ListView):
    model = PostCategory
    template_name = 'forum/forum_list.html'


class ForumDetailView(DetailView):
    model = Post
    template_name = 'forum/forum_detail.html'
