#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/5/26 23:21
# @Author : Tom_tao
# @Site : 
# @File : urls.py
# @Software: PyCharm

from . import views
from django.urls import re_path,path

urlpatterns = [
    path('',views.article),
    # re_path(r'list/(?P<categories>\w+|(\w+\+\w+)+)/',views.article_list)
    path("list/<cate:categories>",views.article_list,name='list'),
    path('detail/<int:article_id>/',views.article_detail,name='detail')
]