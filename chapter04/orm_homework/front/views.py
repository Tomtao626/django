from django.shortcuts import render
from django.http import HttpResponse
from .models import Teacher, Score, Student, Course


def index(request):

    return HttpResponse("successfully")
