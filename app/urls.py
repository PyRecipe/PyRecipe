from django.urls import path

from . import views

app_name = 'app'
urlpatterns = [
    path('', views.index, name='index'),
    path('ayarlar', views.settings, name='settings'),
    path('giris', views.login, name='login'),
    path('kayit', views.signup, name='signup'),
    path('ara', views.searching, name='searching'),
    path('ekle', views.adding, name='adding'),
]