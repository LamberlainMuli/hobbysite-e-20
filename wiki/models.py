from django.db import models
from django.urls import reverse


class ArticleCategory(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank = True)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('wiki:wiki_detail', args=str(self.pk))

    class Meta:
        ordering = ['name']


class Article(models.Model):
    title = models.CharField(max_length=255)
    entry = models.TextField(blank = True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(
         ArticleCategory,
         on_delete=models.SET_NULL,
         null = True,
         default = 1,
         related_name = 'Categories',
    )

    class Meta:
        ordering = ['-created_on']
    
    def __str__(self):
        return f'{self.title} - {self.created_on}'
    
    def get_absolute_url(self):
        return reverse("wiki:wiki_detail", args=str(self.pk))

# Create your models here.
