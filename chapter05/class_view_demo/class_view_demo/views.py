# -*- coding: utf-8 -*-
# @Time : 02/01/2021 20:33
# @Author : tomtao
# @Email : tp320670258@gmail.com
# @File : views.py
# @Project : class_view_demo

from django.http import HttpResponse
from django.views.generic import View, TemplateView
from django.shortcuts import render


def index(request):
    return HttpResponse("success")


class BookListView(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse("book list view")


class AddBookView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'add_book.html')

    def post(self, request, *args, **kwargs):
        book_name = request.POST.get('name')
        book_author = request.POST.get('author')
        print(f"name:{book_name},author:{book_author}")
        return HttpResponse("success")


class BookDetailView(View):
    def get(self, request, book_id):
        print(f"book_id:{book_id}")
        return HttpResponse("success")

    def http_method_not_allowed(self, request, *args, **kwargs):
        return HttpResponse("不支持get以外的请求")


# 如果需要在TemplateView中传递参数，则需要重写
class AboutView(TemplateView):
    template_name = "about.html"

    def get_context_data(self, **kwargs):
        context = {"phone": "123456789"}
        return context
