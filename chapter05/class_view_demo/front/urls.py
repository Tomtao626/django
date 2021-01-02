# -*- coding: utf-8 -*-
# @Time : 02/01/2021 21:15
# @Author : tomtao
# @Email : tp320670258@gmail.com
# @File : urls.py
# @Project : class_view_demo
from django.urls import path

from . import views

app_name = 'front'

urlpatterns = [
    path('add/', views.add_article, name='add_article'),
    path('list/', views.ArticleListView.as_view(), name='article_list'),
    path('login/', views.login, name='login'),
    path('profile/', views.ProfileView.as_view(), name='profile')
]