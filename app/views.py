from django.shortcuts import render, redirect

from .models import Recipe

# homepage
def index(request):
    return render(request, 'index.html')

# settings
def settings(request):
    return render(request, 'settings.html')

# login
def login(request):
    return render(request, 'login.html')

# signup
def signup(request):
    return render(request, 'signup.html')

# searching
def searching(request):
    return render(request, 'searching.html')

# search-listing
def searchListing(request):
    return render(request, 'search-listing.html')

# editing
def editing(request):
    return render(request, 'editing.html')

# adding
def adding(request):
    return render(request, 'adding.html')

# my_recipes
def my_recipes(request):
    return render(request, 'my_recipes.html')

# recipe
def recipe(request, slug):
    try:
        recipe = Recipe.objects.get(slug=slug)
        return render(request, 'recipe.html', {'recipe': recipe})
    except Recipe.DoesNotExist:
        return redirect('/')
