from django.urls import path

from . import views

app_name = 'app'
urlpatterns = [
    path('', views.index, name='index'),
    path('ayarlar', views.settings, name='settings'),
    path('giris', views.userLogin, name='login'),
    path('cikis', views.logout_view, name='logout'),
    path('kayit', views.register, name='register'),
    path('ara', views.search, name='search'),
    path('arama-sonucu', views.searchList, name='search-list'),
    path('duzenle', views.edit, name='edit'),
    path('ekle', views.add, name='add'),
    path('tariflerim', views.MyRecipes.as_view(), name='my_recipes'),
    # if hits /tarif redirect to homepage (/)
    path('tarif/<str:slug>/', views.recipe, name='recipe'),
    path('yorum-sil/<int:comment_id>/', views.delete_comment, name='delete-comment'),
]
