from django.db import models
from django.urls import reverse
from django.utils import timezone


class Commission(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    # should be a positive whole number
    people_required  = models.PositiveIntegerField() 
    created_on = models.DateTimeField(default=timezone.now, blank=True)
    updated_on = models.DateTimeField(default=timezone.now, blank=True)
    
    class Meta:
        ordering = ['created_on']
        
    def __str__(self):
        return f'{self.title}'

    def get_absolute_url(self):
        return reverse('ledger:commission-detail', args=[str(self.pk)])


class Comment(models.Model):
    entry = models.TextField()
    commission = models.ForeignKey(
        Commission,
        on_delete=models.CASCADE, 
        related_name='comments'
    )
    
    created_on = models.DateTimeField(default=timezone.now, blank=True)
    updated_on = models.DateTimeField(default=timezone.now, blank=True)    
    
    class Meta:
        ordering = ['-created_on']
