from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=50)
    price = models.IntegerField(max_length=1000)
    stock = models.IntegerField(max_length=50)
    