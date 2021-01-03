from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import View
from .forms import MyForm, RegisterForm
# Create your views here.
from .models import User


class IndexView(View):
    def get(self, request):
        return render(request, 'index.html')

    def post(self, request):
        form = MyForm(request.POST)
        if not form.is_valid():
            print(form.errors.get_json_data())
            return HttpResponse("fail")
        return HttpResponse("success")


class RegisterView(View):
    def get(self, request):
        return render(request, 'register.html')

    def post(self, request):
        form = RegisterForm(request.POST)
        # 判断数据是否合法
        if not form.is_valid():
            print(form.get_errors())
            return HttpResponse("注册失败")
        username = form.cleaned_data.get('username')
        telephone = form.cleaned_data.get('telephone')
        User.objects.create(username=username, telephone=telephone)
        return HttpResponse("注册成功")