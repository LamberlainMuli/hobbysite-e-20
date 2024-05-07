from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

from user_management.models import User

from .models import ArticleCategory, Article, Comment


class CommentInline(admin.TabularInline):
    model = Comment
    extra = 0  # Number of empty forms to display

class ArticleInline(admin.TabularInline):
    model = Article


class ArticleAdmin(admin.ModelAdmin):
    model = Article
    search_fields = ['title', 'category', 'entry' ,'created_on','updated_on','image']
    list_filter = ['category']
    list_display = ['title',  'category', 'entry' ,'created_on','updated_on', 'image']
    inlines = [CommentInline]



class ArticleCategoryAdmin(admin.ModelAdmin):
    model = Article
    inlines = [ArticleInline]



admin.site.register(Article, ArticleAdmin)
admin.site.register(ArticleCategory,ArticleCategoryAdmin)


# Register your models here.
