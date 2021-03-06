from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import pre_save
from PyRecipe.utils import unique_slug_generator


class Comment(models.Model):
    recipe_id = models.CharField(max_length=30)
    user_id = models.CharField(max_length=30)
    comment = models.TextField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)

    def author_info(self):
        """Returns information about the author"""
        return User.objects.get(pk=self.user_id)


class Recipe(models.Model):
    slug = models.SlugField(max_length=100, blank=True, null=True)
    title = models.CharField(max_length=100, verbose_name="")
    description = models.TextField(
        max_length=800, null=True, blank=True, verbose_name="")
    image = models.ImageField(upload_to='image/', null=True, blank=True,
                              default='image/default_recipe_image.jpg', verbose_name="")
    components = models.TextField(
        max_length=500, null=True, blank=True, verbose_name="")
    # 0 => draft, 1 => public, 2 => private, 3 => deleted
    state = models.IntegerField(default=1, verbose_name="")
    author = models.IntegerField()
    category = models.CharField(max_length=50, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    # If object called without a parameter
    def __str__(self):
        return self.title

    def author_info(self):
        """Returns information about the author"""
        return User.objects.get(pk=self.author)

    # def images_arr(self):
    #     """Returns images as an array"""
    #     if self.images is not None and self.images != "":
    #         return self.images.split(',')
    #     else:
    #         return []

    def components_arr(self):
        """Returns components as an array"""
        if self.components is not None and self.components != "":
            return self.components.split(',')
        else:
            return []

    def first_paragraph(self):
        """Returns first paragraph on description"""
        return self.description.split('\n')[0]


def slug_generator(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)


pre_save.connect(slug_generator, sender=Recipe)
