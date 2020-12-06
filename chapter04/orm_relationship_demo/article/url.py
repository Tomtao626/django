# -*- coding: utf-8 -*-
# @Time : 2020/12/6 21:04
# @Author : tomtao
# @Email : tp320670258@gmail.com
# @File : url.py
# @Project : orm_relationship_demo

from django.urls import path
from . import views

app_name = 'article'

urlpatterns = [
    path('', views.index, name='index'),
    path('delete/', views.delete_view, name='delete'),
    path('one_to_many/', views.one_to_many_view, name='one_to_many')
]
