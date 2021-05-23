from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from django import forms
from .models import Recipe


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name',
                  'email', 'password1', 'password2']


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
    recipe_id = forms.CharField(max_length=30)
    comment = forms.CharField(max_length=500, widget=forms.Textarea)


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


class AddForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ['title', 'description', 'components', 'state', 'image']
        exclude = ['author']

        CHOICES = [('1', 'Herkese Açık'), ('0', 'Gizli')]
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Tarif Adı'
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'style': 'height: 150px',
                'placeholder': 'Yapılışı'
            }),
            'components': forms.Textarea(attrs={
                'class': 'form-control',
                'style': 'height: 100px',
                'placeholder': 'Malzemeler'
            }),
            'state': forms.RadioSelect(choices=CHOICES, attrs={
                'class': 'list-unstyled'
            })
        }


class EditForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ['title', 'description', 'components', 'state', 'image']

        CHOICES = [('1', 'Herkese Açık'), ('0', 'Gizli')]
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Tarif Adı'
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'style': 'height: 150px',
                'placeholder': 'Yapılışı'
            }),
            'components': forms.Textarea(attrs={
                'class': 'form-control',
                'style': 'height: 100px',
                'placeholder': 'Malzemeler'
            }),
            'state': forms.RadioSelect(choices=CHOICES, attrs={
                'class': 'list-unstyled'
            })
        }