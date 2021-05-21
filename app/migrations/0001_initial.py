# Generated by Django 3.2.3 on 2021-05-20 19:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('recipe_id', models.CharField(max_length=30)),
                ('user_id', models.CharField(max_length=30)),
                ('comment', models.TextField(max_length=500)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(blank=True, max_length=100, null=True)),
                ('title', models.CharField(max_length=100, verbose_name='')),
                ('description', models.TextField(blank=True, max_length=800, null=True, verbose_name='')),
                ('image', models.ImageField(blank=True, default='image/default_recipe_image.jpg', null=True, upload_to='image/', verbose_name='')),
                ('components', models.TextField(blank=True, max_length=500, null=True, verbose_name='')),
                ('state', models.IntegerField(default=1, verbose_name='')),
                ('author', models.IntegerField()),
                ('category', models.CharField(blank=True, max_length=50, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
