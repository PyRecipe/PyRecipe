from django.contrib import admin

from .models import Recipe, User

admin.site.register(Recipe)
admin.site.register(User)
