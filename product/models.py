from django.contrib.auth.models import User
from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='uploads/', blank=True, null=True)

    class Meta:
        ordering = ('name', )

    def __str__(self):
        return self.name

    def get_image(self):
        if self.image:
            return "http://127.0.0.1:8000" + self.image.url


class Product(models.Model):
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=6, decimal_places=0)

    class Meta:
        ordering = ('name', )

    def __str__(self):
        return self.name


class Orders(models.Model):
    username_id = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Клиент", blank=True, null=True)
    table = models.DecimalField(max_digits=3, decimal_places=0)
    product_name = models.CharField(max_length=255)
    quantity = models.DecimalField(max_digits=6, decimal_places=0)