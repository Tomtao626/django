# -*- coding: utf-8 -*-
"""
@Time:2021/1/11 23:44
@Auth:Canna
@File:views.py
@IDE:PyCharm
@Motto:626(Always Be Coding)
"""

from django.http import HttpResponse
from django.core.cache import cache


def index(request):
    cache.set('password', 'canna626', 100)
    password = cache.get('password')
    print(password)
    return HttpResponse("pass")

# 查看memcached全部的key
# stats items
# stats cachedump [item_id] 0
