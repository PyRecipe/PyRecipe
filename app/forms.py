from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
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

class EditProfileForm(UserChangeForm):
    class Meta:
        model = User
        fields = (
            'first_name',
            'last_name',
            'email',
        )

class AddForm(forms.Form):
  title = forms.CharField(widget=forms.TextInput(attrs={
    'class': 'form-control',
    'placeholder': 'Tarif Adı'
  }))
  description = forms.CharField(widget=forms.Textarea(attrs={
    'class': 'form-control',
    'style' : 'height: 150px',
    'placeholder': 'Yapılışı'
  }))
  components = forms.CharField(widget=forms.Textarea(attrs={
    'class': 'form-control',
    'style' : 'height: 100px',
    'placeholder': 'Malzemeler'
  }))
  CHOICES=[('1','Herkese Açık'),
         ('0','Gizli')]
  state = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect(attrs={
    'class': 'list-unstyled'
  }))
  image = forms.ImageField()
  
