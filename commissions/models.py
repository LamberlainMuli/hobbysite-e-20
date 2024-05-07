from django.db import models
from django.urls import reverse
from django.utils import timezone


class Commission(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    people_required  = models.PositiveIntegerField() 
    created_on = models.DateTimeField(default=timezone.now, blank=True)
    updated_on = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['created_on']
        
    def __str__(self):
        return f'{self.title}'

    def get_absolute_url(self):
        return reverse('ledger:commission-detail', args=[str(self.pk)])

    def get_word_count(self):
        return len(self.description.split())
    
    def get_read_time(self):
        return self.get_word_count() / 200
    
    def get_date_created(self):
        return self.created_on.strftime('%b %d %Y')
    
    def get_date_updated(self):
        return self.updated_on.strftime('%b %d %Y')

class Comment(models.Model):
    entry = models.TextField()
    commission = models.ForeignKey(
        Commission,
        on_delete=models.CASCADE, 
        related_name='comments'
    )
    
    created_on = models.DateTimeField(default=timezone.now, blank=True)
    updated_on = models.DateTimeField(auto_now=True) 
    
    def get_word_count(self):
        return len(self.entry.split())
    
    def get_read_time(self):
        return self.get_word_count() / 200
    
    def get_date_created(self):
        return self.created_on.strftime('%b %d %Y')
    
    def get_date_updated(self):
        return self.updated_on.strftime('%b %d %Y')
    
    class Meta:
        ordering = ['-created_on']
