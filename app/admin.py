from django.contrib import admin

from .models import Recipe, Comment

# make these tables visible on the admin panel
admin.site.register(Recipe)
admin.site.register(Comment)
