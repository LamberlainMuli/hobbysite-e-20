from django.db import models
from django.urls import reverse

# Create your models here.
class ProductType(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

    def get_word_count(self):
        return len(self.description.split())
    
    def get_read_time(self):
        return self.get_word_count() / 200
    
class Product(models.Model):
    name = models.CharField(max_length=255)
    product_type = models.ForeignKey(ProductType, on_delete=models.SET_NULL, null=True, related_name='type')
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('merchstore:merch_detail', args=str(self.pk))
    
    def get_word_count(self):
        return len(self.description.split())
    
    def get_read_time(self):
        return self.get_word_count() / 200
    