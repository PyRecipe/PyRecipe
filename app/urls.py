from django.urls import path

from . import views

app_name = 'app'
urlpatterns = [
    path('', views.index, name='index'),
    path('ayarlar', views.settings, name='settings'),
    path('ara', views.searching, name='searching'),
    path('tariflerim', views.my_recipes, name='my_recipes')
]
