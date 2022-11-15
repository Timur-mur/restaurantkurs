from django.contrib.auth.models import User
from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        ordering = ('name', )

    def __str__(self):
        return self.name


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