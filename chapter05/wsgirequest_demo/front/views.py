from django.shortcuts import render
from django.http import HttpResponse
from django.core.handlers.wsgi import WSGIRequest
# Create your views here.


def index(request):
    print(request)
    print(type(request))
    return HttpResponse("success")


def login(request):
    print(request.get_host())
    print(request.path)
    print(request.get_full_path())
    print(request.get_raw_uri())
    print(request.META)
    for k,v in request.META.items():
        print(k,v)
    print(request.is_secure()) # 是否使用https
    print(request.is_ajax())  # 是否用ajax
    return HttpResponse("login")
