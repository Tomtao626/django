from django.shortcuts import render

# Create your views here.

from django.shortcuts import render

def index(request):
    return render(request, 'index.html')


def company(request):
    pass


def school(request):
    pass
