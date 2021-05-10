from django.db import models

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
    description = models.TextField(max_length=300)
    images = models.ImageField() # vermedim ancak parametre olarak belirli width,height ve max length değeri verebiliriz.
    components = models.TextField(max_length=500)
    state = models.IntegerField() 
    category = models.CharField(max_length=50)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

