# -*- coding: utf-8 -*-
# @Time : 02/01/2021 23:37
# @Author : tomtao
# @Email : tp320670258@gmail.com
# @File : views.py
# @Project : error_view_demo


from django.http import HttpResponse
from django.shortcuts import render


def view_405(request):
    return render(request, 'errors/405.html', status=405)


def view_403(request):
    return render(request, 'errors/403.html', status=403)