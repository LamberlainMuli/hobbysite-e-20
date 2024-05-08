from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

from user_management.models import Profile


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
    author = models.ForeignKey(
        Profile,
        on_delete=models.SET_NULL,
        null= True,
        related_name = 'Author'
    )
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
    image = models.ImageField(upload_to="images/")
    image_description = models.TextField(max_length=255)

    class Meta:
        ordering = ['-created_on']
    
    def get_author(self):
        return f'{self.author}'
    
    def __str__(self):
        return f'{self.title} - {self.created_on}'
    
    def get_absolute_url(self):
        return reverse("wiki:wiki_detail", args=str(self.pk))
    
    def get_word_count(self):
        return len(self.entry.split())
    
    def get_read_time(self):
        return (self.get_word_count() / 200)
    
    def get_date_created(self):
        return self.created_on.strftime('%b %d %Y')
    
    def get_date_updated(self):
        return self.updated_on.strftime('%b %d %Y')


class Comment(models.Model):
    author = models.ForeignKey(
        Profile,
        on_delete=models.SET_NULL,
        null= True,
        related_name = 'author'
    )
    article =  models.ForeignKey(
        Article,
        on_delete=models.CASCADE,
        null= True,
        related_name = 'article'
    )
    entry = models.TextField(max_length=255)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return f'{self.author} - {self.created_on}'
    
    def get_absolute_url(self):
        return reverse("wiki:wiki_detail", args=str(self.pk))

    
    
# Author - foreign key to Profile who created the comment, set to NULL when deleted
# Article - foreign key to Wiki, model deletion is cascaded
# Entry - text field
# Created On - datetime field, only gets set when the model is created
# Updated On - datetime field, always updates on last model update
# Comments should be sorted by the date it was created, in ascending order
