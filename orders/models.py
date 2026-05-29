from django.db import models
from django.contrib.auth.models import User


class Order(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)

    email = models.EmailField()

    address = models.TextField()

    city = models.CharField(max_length=100)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):

        return self.name


class OrderItem(models.Model):

    order = models.ForeignKey(Order, on_delete=models.CASCADE)

    product_name = models.CharField(max_length=200)

    price = models.DecimalField(max_digits=10, decimal_places=2)

    quantity = models.PositiveIntegerField()

    def __str__(self):

        return self.product_name