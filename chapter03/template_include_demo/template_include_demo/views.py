# -*- coding: utf-8 -*-
# @Time : 2020/11/14 18:37
# @Author : tomtao
# @Email : tp320670258@gmail.com
# @File : views.py
# @Project : django

from django.shortcuts import render


def index(request):
    context = {
        'username': 'tomtao'
    }
    return render(request, 'index.html', context=context)


def company(request):
    return render(request, 'company.html')


def school(request):
    return render(request, 'school.html')
