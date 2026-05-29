from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    name = models.CharField(max_length=200)

    description = models.TextField()

    price = models.DecimalField(max_digits=10, decimal_places=2)

    stock = models.PositiveIntegerField()

    image = models.ImageField(upload_to='products/')

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
# for public reviews
class Review(models.Model):

    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    user = models.ForeignKey(User, on_delete=models.CASCADE)

    comment = models.TextField()

    rating = models.IntegerField()

    created_at = models.DateTimeField(auto_now_add=True)