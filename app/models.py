from django.db import models
from django.utils import timezone

class User(models.Model):
    username = models.CharField(max_length=200)
    fullname = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    confirmed_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    created_at = models.DateTimeField()

class Comment(models.Model):
    recipe_id = models.CharField(max_length=30)
    user_id = models.CharField(max_length=30)
    comment = models.TextField(max_length=500)
    created_at = models.DateTimeField()
    
class Recipe(models.Model):
    slug = models.CharField(max_length=50)
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=300, null=True)
    images = models.TextField(max_length=500, null=True)
    components = models.TextField(max_length=500, null=True)
    state = models.IntegerField(default=0) # 0 => draft, 1 => public, 2 => private, 3 => deleted
    category = models.CharField(max_length=50, null=True)
    created_at = models.DateTimeField(default=timezone.now())
    updated_at = models.DateTimeField(default=timezone.now())
