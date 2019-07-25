from django.db import models
from django.contrib.auth.models import User

class Images(models.Model):
    image = models.ImageField(upload_to="image")

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    stock = models.IntegerField()
    description = models.TextField()
    imgs = models.ManyToManyField(Images)

class Category(models.Model):
    category = models.CharField(max_length=100)
    product = models.ManyToManyField(Product)

class Buyer(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    phone_num = models.CharField(max_length=10)
    address = models.TextField()
    products = models.ManyToManyField(Product)

class Seller(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    phone_num = models.CharField(max_length=10)
    address = models.TextField()
    products = models.ManyToManyField(Product)

class Bill(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    seller = models.ForeignKey(Seller,on_delete=models.CASCADE)
    buyer = models.ForeignKey(Buyer,on_delete=models.CASCADE)   
    qty = models.IntegerField()
    
   