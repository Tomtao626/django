#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/5/26 21:47
# @Author : Tom_tao
# @Site : 
# @File : urls.py
# @Software: PyCharm

from django.urls import path
from . import views

app_name = 'front'

urlpatterns = [
    path('',views.index,name='index'),
    path('signin/',views.login,name='login')
]