# from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import redirect,reverse

def index(request):
    username = request.GET.get('username')
    if username:
        return HttpResponse("cms首页")
    else:
        current_namespace = request.resolver_match.namespace
        return redirect(reverse('%s:login' % current_namespace))

def login(request):
    return HttpResponse("cms登录页面")