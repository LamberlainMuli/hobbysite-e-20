from django.contrib import admin
from .models import Commission, Job, JobApplication, Profile

class JobInline(admin.TabularInline):
    model = Job
    extra = 1  

class JobApplicationInline(admin.TabularInline):
    model = JobApplication
    extra = 1

class CommissionAdmin(admin.ModelAdmin):
    model = Commission
    search_fields = ['title', 'description', 'status']
    list_filter = ['status', 'created_on', 'updated_on']
    list_display = ['title', 'description', 'status', 'created_on', 'updated_on']
    inlines = [JobInline]

class JobAdmin(admin.ModelAdmin):
    model = Job
    search_fields = ['commission__title', 'role', 'status']
    list_filter = ['status', 'manpower_required']
    list_display = ['role', 'commission', 'manpower_required', 'status']
    inlines = [JobApplicationInline]

class JobApplicationAdmin(admin.ModelAdmin):
    model = JobApplication
    search_fields = ['job__role', 'applicant__name', 'status']
    list_filter = ['status', 'applied_on']
    list_display = ['job', 'applicant', 'status', 'applied_on']

class ProfileAdmin(admin.ModelAdmin):
    model = Profile
    search_fields = ['user__username', 'name']
    list_display = ['user', 'name']

admin.site.register(Commission, CommissionAdmin)
admin.site.register(Job, JobAdmin)
admin.site.register(JobApplication, JobApplicationAdmin)
admin.site.register(Profile, ProfileAdmin)
