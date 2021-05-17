from django import forms

class CommentForm(forms.Form):
  recipe_id = forms.CharField(max_length=100)
  comment = forms.CharField(widget=forms.Textarea)