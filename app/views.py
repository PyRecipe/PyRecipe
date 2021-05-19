from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views.generic import ListView
from .forms import CommentForm, CreateUserForm, SearchForm, EditProfileForm
from .models import Recipe, Comment 

# homepage
def index(request):
    return render(request, 'index.html', {'user': request.user})

# settings
def settings(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=request.user)
        print("posta girdi")
        if form.is_valid():
            print("valide girdi")
            form.save()
            return redirect('/')
        
    else:
        form = EditProfileForm()
        print("else e girdi")
        return render(request, 'settings.html', {'user': request.user, 'form': form})


# login
def login(request):
    return render(request, 'login.html', {'user': request.user})

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