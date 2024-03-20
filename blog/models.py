from django.db import models
from django.urls import reverse


class ArticleCategory(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    
    class Meta:
        ordering = ['name'] # order by name ascending order
    

    def __str__(self):
        return self.name


class Article(models.Model):
    title = models.CharField(max_length=255)
    category = models.ForeignKey(ArticleCategory, null=True, on_delete=models.SET_NULL, related_name='article')
    entry = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-created_on'] # order by date created descending  order

    def __str__(self):
        return self.title
   
    def get_absolute_url(self):
        return reverse('blog:article_detail', args=str(self.pk))