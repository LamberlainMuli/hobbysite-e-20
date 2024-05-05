from django.contrib import admin
from.models import Profile, ArticleCategory, Article, Comment

from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User


class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False


class ArticleAdmin(admin.ModelAdmin):
    model = Article


class ArticleCategoryAdmin(admin.ModelAdmin):
    model = ArticleCategory


class CommentAdmin(admin.ModelAdmin):
    model = Comment


class UserAdmin(BaseUserAdmin):
    inlines = [
        ProfileInline,
    ]


admin.site.register(Article, ArticleAdmin)

admin.site.register(ArticleCategory, ArticleCategoryAdmin)

admin.site.unregister(User)

admin.site.register(User, UserAdmin)