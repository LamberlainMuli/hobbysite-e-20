from django.contrib import admin

from .models import Commission, Comment


class CommentInline(admin.TabularInline):
    model = Comment

class CommentAdmin(admin.ModelAdmin):
    model = Comment
    search_fields = ['commission', 'entry', 'created_on', 'updated_on']
    list_filter = ['commission']
    list_display = ['commission', 'entry', 'created_on', 'updated_on']

    # fieldsets = [
    #     ('Comment', {'fields': ['entry']}),
    #     ('Commission', {'fields': ['commission']}),
    # ]

class CommissionAdmin(admin.ModelAdmin):
    model = Commission
    inlines = [CommentInline,]


admin.site.register(Commission, CommissionAdmin)
admin.site.register(Comment, CommentAdmin)