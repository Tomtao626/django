# -*- coding: utf-8 -*-
# @Time : 02/01/2021 23:37
# @Author : tomtao
# @Email : tp320670258@gmail.com
# @File : urls.py
# @Project : error_view_demo
from django.urls import path
from . import views

urlpatterns = [
    path('405.html', views.view_405, name='405'),
    path('403.html', views.view_403, name='403')
]