from django.shortcuts import render, redirect, reverse
from django.views.generic import View
from .forms import RegisterForm, LoginForm
from django.contrib import messages


# Create your views here.
from .models import User


def index(request):
    # user_id = request.session.get('user_id')
    # context = dict()
    # try:
    #     user = User.objects.get(pk=user_id)
    #     context.update(dict(front_user=user))
    # except Exception as e:
    #     print(e)
    users = User.objects.all()
    for user in users:
        print(user)
    return render(request, 'index.html')


class LoginView(View):
    def get(self, request):
        return render(request, 'login.html')

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = User.objects.filter(username=username, password=password).first()
            if user:
                request.session['user_id'] = user.id
                return redirect(reverse('index'))
            else:
                print("用户名或密码错误")
                # messages.add_message(request, messages, INFO, '用户名或密码错误')
                messages.info(request, '用户名或密码错误')
                return redirect(reverse('login'))
        else:
            # print(form.errors.get_json_data())
            errors = form.get_errors()
            for error in errors:
                messages.info(request, error)
            return redirect(reverse('login'))


class RegisterView(View):
    def get(self, request):
        return render(request, 'register.html')

    def post(self, request):
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('index'))
        else:
            # errors = form.errors.get_json_data()
            # print(form.get_errors())
            errors = form.get_errors()
            for error in errors:
                messages.info(request, error)
            return redirect(redirect('register'))


def blog(request):
    return render(request, 'blog.html')


def video(request):
    return render(request, 'video.html')


def logout(request):
    pass
