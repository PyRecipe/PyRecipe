from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views.generic import ListView
from .forms import CommentForm
from .forms import CreateUserForm
from .models import Recipe, Comment

# homepage
def index(request):
    return render(request, 'index.html')

# settings
def settings(request):
    return render(request, 'settings.html')

# login
def login(request):
    return render(request, 'login.html')

# register
def register(request):
    
    if request.method == 'POST':

        user = CreateUserForm(request.POST)
        if user.is_valid():
            user.save()
    else:
        user = CreateUserForm()
        
    context = {'form':user}
    return render(request, 'register.html',context)

# search
def search(request):
    return render(request, 'search.html')

# search-list
def searchList(request):
    return render(request, 'search-list.html')

# edit
def edit(request):
    return render(request, 'edit.html')

# add
def add(request):
    return render(request, 'add.html')

# my_recipes
class MyRecipes(ListView):
    model = Recipe
    template_name = 'my_recipes.html' 

# recipe
def recipe(request, slug):
    try:
        recipe = Recipe.objects.get(slug=slug)
        comments = Comment.objects.filter(recipe_id=recipe.pk)
        if request.method == 'POST':
            form = CommentForm(request.POST)
            if form.is_valid():
                # after auth user id should be dynamicly pasted
                Comment.objects.create(
                  recipe_id = form.cleaned_data['recipe_id'],
                  user_id = 1,
                  comment = form.cleaned_data['comment']
                )
        else:
            form = CommentForm()
        
        return render(request, 'recipe.html', {'recipe': recipe, 'comments': comments, 'form': form})
    except Recipe.DoesNotExist:
        return redirect('/')



