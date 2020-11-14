#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/5/26 21:46
# @Author : Tom_tao
# @Site : 
# @File : urls.py
# @Software: PyCharm
from django.urls import path
from . import views

app_name = 'cms'

urlpatterns = [
    path('',views.index,name='index'),
    path('login/',views.login,name='login')
]