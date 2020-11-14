#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/6/1 22:10
# @Author : Tom_tao
# @Site : 
# @File : views.py
# @Software: PyCharm

from django.shortcuts import render


class Person(object):
    def __init__(self,username):
        self.username = username

def index(request):
    # p = Person("test")
    # context = {
    #     'person':p
    # }
    # context = {
    #     'person':{
    #         'username':'test',
    #         'val':'abc',
    #     }
    # }
    # context = {
    #     'person':[
    #         '鲁班',
    #         '张飞',
    #         '诸葛亮',
    #     ]
    # }  根据列表下标获取
    context = {
        'person': (
            '鲁班',
            '张飞',
            '诸葛亮',
        )
    }
    # 根据元组下标获取
    return render(request, 'index.html', context=context)