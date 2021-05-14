from django.urls import path

from . import views

app_name = 'app'
urlpatterns = [
    path('', views.index, name='index'),
    path('ayarlar', views.settings, name='settings'),
    path('giris', views.login, name='login'),
    path('kayit', views.signup, name='signup'),
    path('ara', views.searching, name='searching'),
    path('arama-sonuclari', views.searchListing, name='search-listing'),
    path('duzenle', views.editing, name='editing'),
    path('ekle', views.adding, name='adding'),
    path('tariflerim', views.my_recipes, name='my_recipes'),
    path('tarif/<str:slug>/', views.recipe, name='recipe'),
]
