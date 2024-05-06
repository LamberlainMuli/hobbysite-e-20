from django import forms
from .models import Commission, Job, JobApplication, Profile

class CommissionForm(forms.ModelForm):
    class Meta:
        model = Commission
        fields = ['title', 'description', 'status']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
        }
        labels = {
            'title': 'Commission Title',
            'description': 'Detailed Description',
            'status': 'Current Status',
        }

class CommissionUpdateForm(forms.ModelForm):
    class Meta:
        model = Commission
        fields = ['title', 'description', 'status']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
        }
        labels = {
            'title': 'Update Title',
            'description': 'Update Description',
            'status': 'Update Status',
        }

class JobForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = ['role', 'manpower_required', 'status']
        widgets = {
            'role': forms.TextInput(attrs={'class': 'form-control'}),
            'manpower_required': forms.NumberInput(attrs={'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
        }
        labels = {
            'role': 'Role Description',
            'manpower_required': 'Manpower Needed',
            'status': 'Current Status',
        }

class JobCreateForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = ['commission', 'role', 'manpower_required', 'status']
        widgets = {
            'commission': forms.HiddenInput(),
            'role': forms.TextInput(attrs={'class': 'form-control'}),
            'manpower_required': forms.NumberInput(attrs={'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
        }
        labels = {
            'role': 'Role Description',
            'manpower_required': 'Manpower Needed',
            'status': 'Current Status',
        }

class JobApplicationForm(forms.ModelForm):
    class Meta:
        model = JobApplication
        fields = ['job', 'applicant', 'status']
        widgets = {
            'job': forms.Select(attrs={'class': 'form-control'}),
            'applicant': forms.Select(attrs={'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
        }
        labels = {
            'job': 'Job Position',
            'applicant': 'Applicant Name',
            'status': 'Application Status',
        }

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['user', 'name', 'bio']
        widgets = {
            'user': forms.HiddenInput(),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'bio': forms.Textarea(attrs={'class': 'form-control'}),
        }
        labels = {
            'name': 'Full Name',
            'bio': 'Biography',
        }
