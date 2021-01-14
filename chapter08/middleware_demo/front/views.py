from django.shortcuts import render, redirect, reverse
from django.views.generic import View
from django.contrib import messages
from django.http import HttpResponse

# Create your views here.
from .models import User


def index(request):
    # print('这是index view中执行的代码')
    # if request.front_user:
    #     print(request.front_user.username)
    # return HttpResponse("index")
    return render(request, 'index.html')


def my_list(request):
    print('这是my_list view中执行的代码')
    if request.front_user:
        print(request.front_user.username)
    return HttpResponse("my_list")


class LoginView(View):
    def get(self, request):
        return render(request, 'login.html')

    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = User.objects.filter(username=username, password=password).first()
        if user:
            request.session['user_id'] = user.id
            return redirect(reverse('index'))
        else:
            print("用户名或密码错误")
            # messages.add_message(request, messages, INFO, '用户名或密码错误')
            messages.info(request, '用户名或密码错误')
            return redirect(reverse('login'))
