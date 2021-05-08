from django.db import models

class User(models.Model):
    username = models.CharField(max_length=200)
    fullname = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    confirmed_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    created_at = models.DateTimeField()
