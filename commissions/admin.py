from django.contrib import admin

from .models import Commission, Comment


class CommentInline(admin.TabularInline):
    model = Comment

class CommentAdmin(admin.ModelAdmin):
    model = Comment
    search_fields = ['commission', 'entry', 'created_on', 'updated_on']
    list_filter = ['commission']
    list_display = ['commission', 'entry', 'created_on', 'updated_on']


class CommissionAdmin(admin.ModelAdmin):
    model = Commission
    search_fields = ['title', 'description', 'people_required', 'created_on', 'updated_on']
    list_filter = ['created_on', 'updated_on']
    list_display = ['title', 'description', 'people_required', 'created_on', 'updated_on']
    inlines = [CommentInline,]

    


admin.site.register(Commission, CommissionAdmin)
admin.site.register(Comment, CommentAdmin)