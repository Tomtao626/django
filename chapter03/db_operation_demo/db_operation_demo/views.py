# -*- coding: utf-8 -*-
# @Time : 2020/11/16 23:41
# @Author : tomtao
# @Email : tp320670258@gmail.com
# @File : views.py
# @Project : db_operation_demo

from django.shortcuts import render
from django.db import connection


def index(request):
    cursor = connection.cursor()
    cursor.execute("insert into book(id,name,author) values(null, '三国演义','罗贯中')")
    cursor.execute("select * from book")
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    return render(request, 'index.html')
