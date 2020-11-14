#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/5/26 21:04
# @Author : Tom_tao
# @Site : 
# @File : urls.py
# @Software: PyCharm
from django.urls import path
from . import views

# app_name = 'book'

urlpatterns = [
    path('',views.book),
    path('detail/<book_id>',views.book_detail),
    path('list/',views.book_list)
]