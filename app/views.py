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

# searching
def searching(request):
    return render(request, 'searching.html')