from django.db import models
from django.contrib.auth.models import User
# Create your models here.

# models for pizza
class Pizza_type(models.Model): # regular, sicilian, etc..
    pizza_type = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return f"{self.pizza_type}"


class Pizza_topping_number(models.Model): # cheese, 1 topping, etc...
    pizza_topping_number = models.CharField(max_length=50, unique=True)
    topping_number = models.IntegerField()

    def __str__(self):
        return f"{self.pizza_topping_number} - {self.topping_number}"


class Pizza_topping(models.Model): # list of avaiable topping
    pizza_topping = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return f"{self.pizza_topping}"


class Pizza(models.Model):
    pizza_type = models.ForeignKey(Pizza_type, on_delete=models.CASCADE)
    pizza_topping_number = models.ForeignKey(Pizza_topping_number, on_delete=models.CASCADE)
    small_price = models.DecimalField(max_digits=30, decimal_places=2, null=True, blank=True)
    large_price = models.DecimalField(max_digits=30, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return f"{self.pizza_type} - {self.pizza_topping_number} - S: {self.small_price} - L: {self.large_price}"


# models for subs
class Sub(models.Model):
    sub = models.CharField(max_length=50, unique=True)
    small_price = models.DecimalField(max_digits=30, decimal_places=2, null=True, blank=True)
    large_price = models.DecimalField(max_digits=30, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return f"{self.sub} - S: {self.small_price} - L: {self.large_price}"


class Sub_extra(models.Model):
    sub_extra = models.CharField(max_length=50, unique=True)
    small_price = models.DecimalField(max_digits=30, decimal_places=2, null=True, blank=True)
    large_price = models.DecimalField(max_digits=30, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return f"{self.sub_extra} - {self.small_price} - {self.large_price}"


# model for pasta
class Pasta(models.Model):
    item = models.CharField(max_length=50, unique=True)
    price = models.DecimalField(max_digits=30, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return f"{self.item} - {self.price}"


# model for salad
class Salad(models.Model):
    item = models.CharField(max_length=50, unique=True)
    price = models.DecimalField(max_digits=30, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return f"{self.item} - {self.price}"


# model for dinner platter
class Dinner_platter(models.Model):
    dinner_platter = models.CharField(max_length=50, unique=True)
    small_price = models.DecimalField(max_digits=30, decimal_places=2, null=True, blank=True)
    large_price = models.DecimalField(max_digits=30, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return f"{self.dinner_platter} - S: {self.small_price} - L: {self.large_price}"


# shopping cart
class Shopping_cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    item = models.CharField(max_length=100)
    note = models.TextField(blank=True)
    price = models.DecimalField(max_digits=30, decimal_places=2)
    quantity = models.IntegerField()

    def total(self):
        return self.price * self.quantity

    def __str__(self):
        return f"[{self.user}] {self.item} - {self.note} - {self.price} - {self.quantity}"

# transaction history
class Transaction(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    item = models.CharField(max_length=100)
    note = models.TextField(blank=True)
    price = models.DecimalField(max_digits=30, decimal_places=2)
    quantity = models.IntegerField()
    date = models.DateTimeField(auto_now_add=True)
    delivered = models.BooleanField(default=False)

    def total(self):
        return self.price * self.quantity

    def __str__(self):
        return f"[{self.date}] [{self.user}] {self.item} - {self.note} - ${self.price} - Quantity: {self.quantity} (${self.total()}) - Delivered: {self.delivered}"
