from django.shortcuts import render

# Create your views here.

def create(request):
    return render(request, 'create.html')

def location(request):
    return render(request, 'location.html')

def data(request):
    return render(request, 'data.html')
