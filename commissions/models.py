from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.models import User

class Commission(models.Model):
    STATUS_CHOICES = [
        ('Open', 'Open'),
        ('Full', 'Full'),
        ('Completed', 'Completed'),
        ('Discontinued', 'Discontinued'),
    ]
    
    creator = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    title = models.CharField(max_length=255)
    description = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Open')
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['created_on']
        
    def __str__(self):
        return f'{self.title}'

    def get_absolute_url(self):
        return reverse('commissions:commission-detail', args=[str(self.pk)])

    def get_word_count(self):
        return len(self.description.split())
    
    def get_read_time(self):
        return self.get_word_count() / 200
    
    def get_date_created(self):
        return self.created_on.strftime('%b %d %Y')
    
    def get_date_updated(self):
        return self.updated_on.strftime('%b %d %Y')

class Job(models.Model):
    STATUS_CHOICES = [
        ('Open', 'Open'),
        ('Full', 'Full'),
    ]

    
    commission = models.ForeignKey(Commission, on_delete=models.CASCADE, related_name='jobs')
    role = models.CharField(max_length=255)
    manpower_required = models.PositiveIntegerField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='Open')
    
    def get_word_count(self):
        return len(self.entry.split())
    
    def get_read_time(self):
        return self.get_word_count() / 200
    
    def get_date_created(self):
        return self.created_on.strftime('%b %d %Y')
    
    def get_date_updated(self):
        return self.updated_on.strftime('%b %d %Y')
    
    class Meta:
        ordering = ['status', '-manpower_required', 'role']
    
    def __str__(self):
        return f'{self.role} in {self.commission}'


class JobApplication(models.Model):
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Accepted', 'Accepted'),
        ('Rejected', 'Rejected'),
    ]

    job = models.ForeignKey(Job, on_delete=models.CASCADE, related_name='applications')
    applicant = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='Pending')
    applied_on = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['status', '-applied_on']
    
    def __str__(self):
        return f'{self.applicant} - {self.status}'
