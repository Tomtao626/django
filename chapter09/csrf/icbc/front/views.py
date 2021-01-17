from django.db.models import F
from django.http import HttpResponse
from django.shortcuts import render, redirect, reverse
from .models import User

# Create your views here.
from django.views.generic import View
from .forms import RegisterForm, LoginForm, TransferForm


def index(request):
    return render(request, 'index.html')


class LoginView(View):
    def get(self, request):
        return render(request, 'login.html')

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            user = User.objects.filter(email=email, password=password).first()
            if user:
                request.session['user_id'] = user.pk
                return redirect(reverse('index'))
            else:
                print("邮箱或密码错误")
                return redirect(reverse('login'))
        else:
            print(form.errors)
            return redirect(reverse('login'))


class RegisterView(View):
    def get(self, request):
        return render(request, 'register.html')

    def post(self, request):
        form = RegisterForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            username = form.cleaned_data.get('username')
            User.objects.create(email=email, password=password, username=username, balance=1000)
            return redirect(reverse('login'))
        else:
            print(form.errors)
            return redirect(reverse('register'))


class TransferView(View):
    def get(self, request):
        return render(request, 'transfer.html')

    def post(self, request):
        form = TransferForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            money = form.cleaned_data.get('money')
            user_id = request.session.get('user_id')
            user = User.objects.get(pk=user_id)
            if user.balance >= money:
                # to_user = User.objects.filter(email=email).first()
                # to_user.balance += money
                User.objects.filter(email=email).update(balance=F('balance') + money)
                user.balance -= money
                user.save()
                return HttpResponse("转账成功")
            else:
                return HttpResponse("余额不足")
        else:
            print(form.errors)
            return redirect(reverse('transfer'))


def logout(request):
    request.session.flush()
    return redirect(reverse('index'))