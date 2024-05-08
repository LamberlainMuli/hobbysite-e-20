from django.db import models
from django.urls import reverse


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

    product_status = {
        "Available": "Available",
        "On Sale": "On Sale",
        "Out of Stock": "Out of Stock",
    }

    name = models.CharField(max_length=255)
    type = models.ForeignKey(
        ProductType,
        on_delete=models.SET_NULL,
        related_name="products",
        null=True,
    )
    owner = models.ForeignKey(
        "user_management.Profile",
        on_delete=models.CASCADE,
        related_name="products",
    )
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()
    status = models.CharField(max_length=32, choices=product_status)

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
    
    def save(self):
        if self.stock <= 0:
            self.status = "Out of Stock"
        else:
            self.status = "Available"
        return super().save()


class Transaction(models.Model):

    transaction_status = {
        "On Cart": "On Cart",
        "To Pay": "To Pay",
        "To Ship": "To Ship",
        "To Receive": "To Receive",
        "Delivered": "Delivered",
    }

    buyer = models.ForeignKey(
        "user_management.Profile",
        on_delete=models.SET_NULL,
        null=True,
    )
    product = models.ForeignKey(
        Product,
        on_delete=models.SET_NULL,
        null=True,
    )
    amount = models.IntegerField()
    status = models.CharField(max_length=32, choices=transaction_status)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.amount} - {self.product} - {self.status}"
    
    def get_absolute_url(self):
        return reverse("merchstore:transaction_detail", kwargs={"pk": self.pk})
    