from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'index.html')

def name(request):
    userName = request.GET['name']
    return render(request, 'name.html', {'userName':userName})
