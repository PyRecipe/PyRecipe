from django.shortcuts import render

# homepage
def index(request):
    return render(request, 'index.html')

# settings
def settings(request):
    return render(request, 'settings.html')

# searching
def searching(request):
    return render(request, 'searching.html')
