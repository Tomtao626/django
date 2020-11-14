#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/5/26 22:41
# @Author : Tom_tao
# @Site : 
# @File : urls.py
# @Software: PyCharm

from django.urls import re_path
from . import views

urlpatterns = [
    # r'' 代表的是原生字符串raw
    re_path(r'^$',views.article),
    re_path(r"^list/(?P<year>\d{4}/$)",views.article_list),
    re_path(r"^list/(?P<month>\d{2}/$)",views.article_list_month),
]