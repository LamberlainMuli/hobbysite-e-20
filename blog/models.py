from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User



class ArticleCategory(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

    class Meta:
        ordering = ['name'] # order by name ascending order
    

    def __str__(self):
        return self.name
    

class Article(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(User, null=True, on_delete=models.SET_NULL, related_name='article')
    category = models.ForeignKey(ArticleCategory, null=True, on_delete=models.SET_NULL, related_name='article')
    entry = models.TextField()
    
    image = models.ImageField(upload_to="images/")
    image_description = models.TextField(max_length = 255)
    
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-created_on'] # order by date created descending  order

    def __str__(self):
        return self.title
   
    def get_absolute_url(self):
        return reverse('blog:article_detail', args=str(self.pk))
    
    def get_word_count(self):
        return len(self.entry.split())
    
    def get_read_time(self):
        return self.get_word_count() / 200
    
    def get_date_created(self):
        return self.created_on.strftime('%b %d, %Y')
    
    def get_date_updated(self):
        return self.updated_on.strftime('%b %d, %Y')

class Comment(models.Model):
    author = models.ForeignKey(User, null=True, on_delete=models.SET_NULL, related_name='comment')
    article = models.ForeignKey(Article, null=True, on_delete=models.CASCADE, related_name='comment')
    entry = models.TextField(max_length=255)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['created_on'] # order by date created ascending  order

    def __str__(self):
        return f'{self.author} - {self.created_on}'
  
    def get_absolute_url(self):
        return reverse('blog:article_detail', args=str(self.pk))
