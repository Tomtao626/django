#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/6/1 22:47
# @Author : Tom_tao
# @Site : 
# @File : views.py
# @Software: PyCharm

from django.shortcuts import render


def index(request):
    context = {
        # 'books':[
        #     '三国演义',
        #     '红楼梦',
        #     '西游记',
        #     '水浒传',
        # ],
        'books': [
            {
                'name': '三国演义',
                'author': '罗贯中',
                'price': 199,
            },
            {
                'name': '水浒传',
                'author': '施耐庵',
                'price': 99,
            },
            {
                'name': '西游记',
                'author': '吴承恩',
                'price': 299,
            },
            {
                'name': '红楼梦',
                'author': '曹雪芹',
                'price': 999,
            },
        ],
        "person": {
            'username': 'tomtao',
            'age': 18,
            'career': 'doctor',
        },
        'comments':[
            # '文章真好',
            # '确实好',
        ]
    }
    return render(request, "index.html", context=context)
