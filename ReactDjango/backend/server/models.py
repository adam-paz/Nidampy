from django.conf import settings
from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
# Create your models here.


class Profile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    birth_date = models.DateField(null=True, blank=True) 
    

class Order(models.Model):
    created = models.DateField( auto_now=False, auto_now_add=False)
    modified = models.DateField( auto_now=False, auto_now_add=False)
    status = models.CharField( max_length=50)
    amount = models.IntegerField()
    user = models.ForeignKey(Profile, related_name='orders', on_delete=models.CASCADE) 

class OrderItem(models.Model):
    quantity = models.IntegerField()
    product = models.CharField(max_length=50)
    order = models.ForeignKey(Order, related_name='orderItems', on_delete=models.CASCADE) 
    

class Board(models.Model):
    name = models.CharField(max_length=30, unique=True)
    description = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Topic(models.Model):
    subject = models.CharField(max_length=255)
    last_updated = models.DateTimeField(auto_now_add=True)
    board = models.ForeignKey(Board, related_name='topics',  on_delete = models.CASCADE)
    starter = models.ForeignKey(User, related_name='topics', on_delete = models.CASCADE)


class Post(models.Model):
    message = models.TextField(max_length=4000)
    topic = models.ForeignKey(Topic, related_name='posts', on_delete = models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True)
    created_by = models.ForeignKey(User, related_name='posts', on_delete = models.CASCADE)
    updated_by = models.ForeignKey(User, null=True, related_name='+', on_delete = models.CASCADE)
