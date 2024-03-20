from django.contrib import admin

from .models import ArticleCategory, Article


class ArticleInline(admin.TabularInline):
    model = Article


class ArticleAdmin(admin.ModelAdmin):
    model = Article
    search_fields = ['title', 'category', 'entry' ,'created_on','updated_on']
    list_filter = ['category']
    list_display = ['title',  'category', 'entry' ,'created_on','updated_on']


class ArticleCategoryAdmin(admin.ModelAdmin):
    model = Article
    inlines = [ArticleInline]


admin.site.register(Article, ArticleAdmin)
admin.site.register(ArticleCategory,ArticleCategoryAdmin)
# Register your models here.
