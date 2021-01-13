#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author:tom_tao626 
@license: Apache Licence 
@file: views.py 
@time: 2021/01/12
@contact: tp320670258@gmail.com
@site: xxxx.suizhu.net
@software: PyCharm 
"""

from django.http import HttpResponse
from datetime import datetime
from django.utils.timezone import make_aware


def index(request):
    response = HttpResponse("index")
    expires = datetime(year=2021, month=1, day=12, hour=14, minute=0, second=0)
    # response.set_cookie("username", "canna", max_age=300)
    # 时区修正
    expires = make_aware(expires)
    # response.set_cookie("password", "tomtao626", expires=expires)  # 如果expire和max_age都设置了 会以expire为主， 建议使用max_age
    # 如果要设置某个cookie信息只在某个路径下可用 可使用path参数指定
    response.set_cookie("user_id", "66666", expires=expires, path='/cms/')
    return response


def my_list(request):
    cookies = request.COOKIES
    print(cookies)
    password = cookies.get('password')
    print(password)
    # 不在该路由下的cookie 直接获取会返回None
    user_id = cookies.get('user_id')
    return HttpResponse(user_id)


def cms_view(request):
    cookies = request.COOKIES
    print(cookies)
    password = cookies.get('password')
    print(password)
    # 由于user_id是该路由下的cookie 直接获取会返回user_id对应的值
    user_id = cookies.get('user_id')
    return HttpResponse(user_id)


def delete_cookie(request):
    response = HttpResponse("delete")
    response.delete_cookie("password")
    return response
