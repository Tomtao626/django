#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/6/2 23:41
# @Author : Tom_tao
# @Site : 
# @File : views.py
# @Software: PyCharm

from django.shortcuts import render

def index(request):
    return render(request,"index.html")