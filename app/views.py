from django.shortcuts import render

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

# adding
def adding(request):
    return render(request, 'adding.html')