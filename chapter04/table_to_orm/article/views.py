from django.http import HttpResponse
from django.shortcuts import render
from .models import Article, Tag
from front.models import User

# Create your views here.

def index(request):

    return HttpResponse("success")
