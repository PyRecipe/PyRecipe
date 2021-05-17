from django.shortcuts import render, redirect
from .models import Recipe, Comment
from .forms import SearchForm

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
    return render(request, 'register.html')

# search
def search(request):
    if request.method == 'GET':
        return render(request, 'search.html')
    elif request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            search = form.cleaned_data['search']
            results = Recipe.objects.filter(title__contains=search)
            return render(request, 'search-list.html', {'query': search, 'results': results})

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
def my_recipes(request):
    return render(request, 'my_recipes.html')

# recipe
def recipe(request, slug):
    try:
        recipe = Recipe.objects.get(slug=slug)
        comments = Comment.objects.filter(recipe_id=recipe.pk)
        return render(request, 'recipe.html', {'recipe': recipe, 'comments': comments})
    except Recipe.DoesNotExist:
        return redirect('/')
