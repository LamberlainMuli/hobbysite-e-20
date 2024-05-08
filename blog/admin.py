from django.contrib import admin
from.models import  ArticleCategory, Article, Comment

from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User



class ArticleAdmin(admin.ModelAdmin):
    model = Article


class ArticleCategoryAdmin(admin.ModelAdmin):
    model = ArticleCategory


class CommentAdmin(admin.ModelAdmin):
    model = Comment



admin.site.register(Article, ArticleAdmin)

admin.site.register(ArticleCategory, ArticleCategoryAdmin)

