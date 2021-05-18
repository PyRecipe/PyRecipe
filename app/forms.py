from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email','password1','password2']

class LoginForm(forms.Form):
  username = forms.CharField(widget=forms.TextInput(attrs={
    'class': 'form-control',
    'placeholder': 'Kullanıcı Adı'
  }))
  password = forms.CharField(widget=forms.PasswordInput(attrs={
    'class': 'form-control',
    'placeholder': 'Şifre'
  }))

class CommentForm(forms.Form):
  recipe_id = forms.CharField(max_length=100)
  comment = forms.CharField(widget=forms.Textarea)

class SearchForm(forms.Form):
   search = forms.CharField(max_length=200)