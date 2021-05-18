from django.shortcuts import render, redirect
from .models import Recipe, Comment
from .forms import SearchForm

# homepage
def index(request):
    return render(request, 'index.html', {'user': request.user})

# settings
def settings(request):
    return render(request, 'settings.html', {'user': request.user})

# login
def login(request):
    return render(request, 'login.html', {'user': request.user})

# register
def register(request):
    return render(request, 'register.html', {'user': request.user})

# search
def search(request):
    if request.method == 'GET':
        return render(request, 'search.html')
    elif request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            search = form.cleaned_data['search']
            if "," in search:
                # user is searching with components
                search_stripped = "".join(search.split())
                components = set([x.lower() for x in search_stripped.split(",") if x.strip()])
                results = []
                for recipe in Recipe.objects.all():
                    recipe_components_stripped = "".join(recipe.components.split())
                    recipe_components = set([x.lower() for x in recipe_components_stripped.split(",") if x.strip()])
                    if components.issubset(recipe_components) or components == recipe_components:
                        results.append(recipe)
            else:
                # user is searching with recipe name
                results = Recipe.objects.filter(title__contains=search)
            return render(request, 'search-list.html', {'query': search, 'results': results, 'user': request.user})
        else:
            return redirect('/')

# search-list
def searchList(request):
    return render(request, 'search-list.html', {'user': request.user})

# edit
def edit(request):
    return render(request, 'edit.html', {'user': request.user})

# add
def add(request):
    return render(request, 'add.html', {'user': request.user})

# my_recipes
def my_recipes(request):
    return render(request, 'my_recipes.html', {'user': request.user})

# recipe
def recipe(request, slug):
    try:
        recipe = Recipe.objects.get(slug=slug)
        comments = Comment.objects.filter(recipe_id=recipe.pk)
        return render(request, 'recipe.html', {'recipe': recipe, 'comments': comments, 'user': request.user})
    except Recipe.DoesNotExist:
        return redirect('/')
