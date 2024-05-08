from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


class ThreadCategory(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name
   
    def get_absolute_url(self):
        return reverse('forum:forum_detail', args=str(self.pk))


class Thread(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(User, null=True, on_delete=models.SET_NULL, related_name='post')
    category = models.ForeignKey(
        ThreadCategory,
        on_delete=models.SET_NULL,
        null=True,
        related_name='post')
    entry = models.TextField()
    image = models.ImageField(upload_to="images/", null=True, blank=True)
    image_description = models.TextField(max_length=255, null=True, blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return f'{self.title}'
   
    def get_absolute_url(self):
        return reverse('forum:forum_detail', args=str(self.pk))
    
    def get_word_count(self):
        return len(self.entry.split())
    
    def get_read_time(self):
        return (self.get_word_count() / 200)
    
    def get_date_created(self):
        return self.created_on.strftime('%b %d %Y')
    
    def get_date_updated(self):
        return self.updated_on.strftime('%b %d %Y')
    

class Comment(models.Model):
    author = models.ForeignKey(User, null=True, on_delete=models.SET_NULL, related_name='comment')
    thread = models.ForeignKey(Thread, null=True, on_delete=models.CASCADE, related_name='comment')
    entry = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return f'{self.author} - {self.created_on}'
  
    def get_absolute_url(self):
        return reverse('forum:forum_detail', args=str(self.pk))

