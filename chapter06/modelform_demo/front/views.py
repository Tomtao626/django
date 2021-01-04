from django.http import HttpResponse
from django.shortcuts import render
from .forms import AddBookForm, RegisterForm
# Create your views here.


def index(request):
    return HttpResponse("success")


def add_book(request):
    form = AddBookForm(request.POST)
    if not form.is_valid():
        print(form.errors.get_json_data)
        return HttpResponse('fail')
    # title = form.cleaned_data.get('title')
    # page = form.cleaned_data.get('page')
    # price = form.cleaned_data.get('price')
    # print(title)
    # print(page)
    # print(price)
    form.save()
    return HttpResponse('success')


def register(request):
    form = RegisterForm(request.POST)
    if not form.is_valid():
        print(form.errors.get_json_data())
        return HttpResponse("fail")
    user = form.save(commit=False)
    user.password = form.cleaned_data.get('pwd1')
    user.save()
    return HttpResponse("success")