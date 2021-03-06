from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views.generic import ListView
from .forms import CommentForm, CreateUserForm, SearchForm, LoginForm, EditProfileForm, AddForm, EditForm
from .models import Recipe, Comment
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages

# homepage
def index(request):
    # get latest 10 recipes
    latest_recipes = Recipe.objects.all()[:10]
    return render(request, 'index.html', {'user': request.user, 'latest_recipes': latest_recipes})

# settings
@login_required()
def settings(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.info(
                    request, 'Ayarlar Güncellendi.')
    else:
        form = EditProfileForm(instance=request.user)
        
    return render(request, 'settings.html', {'user': request.user, 'form': form})

# login
def userLogin(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            form = LoginForm(request.POST)
            if form.is_valid():
                username = form.cleaned_data['username']
                password = form.cleaned_data['password']
                user = authenticate(request, username=username, password=password)

                if user is not None:
                    if user.is_active:
                        login(request, user)
                        return redirect('/')
                    else:
                        messages.info(request, 'Hesap Devre Dışı')
                else:
                    messages.info(
                        request, 'Kullanıcı adı ve şifrenizi kontrol edin.')
        else:
            form = LoginForm()

        return render(request, 'login.html', {'form': form, 'user': request.user})
    else:
        return redirect('/')

# logout
@login_required()
def logout_view(request):
    logout(request)
    return redirect('/')

# register
def register(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            user = CreateUserForm(request.POST)
            if user.is_valid():
                user.save()
                messages.info(
                        request, 'Hesap oluşturuldu. Giriş yapabilirsin.')
                return redirect('/giris')
            else:
                    messages.info(
                        request, 'Girdiğiniz bilgileri kontrol edin.')
        else:
            user = CreateUserForm()

        return render(request, 'register.html', {'form': user, 'user': request.user})
    else:
        return redirect('/')

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
                components = set(
                    [x.lower() for x in search_stripped.split(",") if x.strip()])
                results = []
                for recipe in Recipe.objects.all():
                    recipe_components_stripped = "".join(
                        recipe.components.split())
                    recipe_components = set(
                        [x.lower() for x in recipe_components_stripped.split(",") if x.strip()])
                    if components.issubset(recipe_components) or components == recipe_components:
                        results.append(recipe)
            else:
                # user is searching with recipe name
                results = Recipe.objects.filter(title__icontains=search.lower())
            return render(request, 'search-list.html', {'query': search, 'results': results, 'user': request.user})
        else:
            return redirect('/')

# search-list
def searchList(request):
    return render(request, 'search-list.html', {'user': request.user})

# edit
@login_required()
def edit(request, slug):
    recipe = Recipe.objects.get(slug=slug)

    if request.user.pk == recipe.author:
        if request.method == "POST":
            form = EditForm(request.POST, request.FILES, instance=recipe)

            if form.is_valid():
                form.save()
                return redirect('/tariflerim')

        else:
            form = EditForm(instance=recipe)
    else:
        form = EditForm(instance=recipe)

    return render(request, 'edit.html', {'user': request.user, 'form': form, 'recipe': recipe})

# add
@login_required()
def add(request):
    if request.method == "POST":
        form = AddForm(request.POST, request.FILES)

        if form.is_valid():
            form.instance.author = request.user.pk
            form.save()
            return redirect('/tariflerim')
    else:
        form = AddForm()
    return render(request, 'add.html', {'form': form, 'user': request.user})

# my_recipes
class MyRecipes(LoginRequiredMixin, ListView):
    model = Recipe
    template_name = 'my_recipes.html'

# delete_recipe
@login_required()
def delete_recipe(request, slug):

    recipe = Recipe.objects.get(slug=slug)

    if request.user.pk is not None:
        if recipe is not None:
            recipe.delete()

    return redirect(f'/tariflerim')

# delete_comment
@login_required()
def delete_comment(request, comment_id):
    # get information about recipe and comment
    comment = Comment.objects.get(pk=comment_id)
    recipe = Recipe.objects.get(pk=comment.recipe_id)

    if request.user.pk is not None:
        if comment is not None:
            # if the author is the logged in user
            if comment.user_id == str(request.user.pk):
                comment.delete()

    # return previous page
    return redirect(f'/tarif/{recipe.slug}')

# recipe
def recipe(request, slug):
    try:
        recipe = Recipe.objects.get(slug=slug)
        comments = Comment.objects.filter(recipe_id=recipe.pk)
        if recipe.state == 1 or recipe.author == request.user.pk:
            if request.method == 'POST':
                form = CommentForm(request.POST)
                if form.is_valid():
                    # after auth user id should be dynamicly pasted
                    Comment.objects.create(
                        recipe_id=form.cleaned_data['recipe_id'],
                        user_id=request.user.pk,
                        comment=form.cleaned_data['comment']
                    )
            else:
                form = CommentForm()

            return render(request, 'recipe.html', {'recipe': recipe, 'comments': comments, 'form': form})
        else:
            return redirect('/')
    except Recipe.DoesNotExist:
        return redirect('/')
