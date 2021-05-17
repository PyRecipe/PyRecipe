from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email','password1','password2']

        
class CommentForm(forms.Form):
  recipe_id = forms.CharField(max_length=100)
  comment = forms.CharField(widget=forms.Textarea)

