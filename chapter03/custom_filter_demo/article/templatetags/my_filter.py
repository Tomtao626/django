# -*- coding: utf-8 -*-
# @Time : 2020/11/14 17:31
# @Author : tomtao
# @Email : tp320670258@gmail.com
# @File : my_filter.py
# @Project : django

from django import template
from datetime import datetime

register = template.Library()


# 过滤器最多只能有两个参数
# 过滤器的第一个参数永远都是被过滤的那个参数（也就是竖线左边的那个参数）
@register.filter('my_greet')
def greet(value, word):
    return value + word

# register.filter("greet", greet)

@register.filter
def time_since(value):
    """
    time距离现在的时间间隔
    1. 如果时间间隔小于1分钟以内，那么就显示“刚刚”
    2. 如果是大于1分钟小于1小时，那么就显示“xx分钟前”
    3. 如果是大于1小时小于24小时，那么就显示“xx小时前”
    4. 如果是大于24小时小于30天以内，那么就显示“xx天前”
    5. 否则就是显示具体的时间 2017/10/20 16:15
    :param value:
    :return:
    """
    if not isinstance(value,datetime):
        return value
    now = datetime.now()
    # timedelay.total_seconds
    timestamp = (now - value).total_seconds()
    if timestamp < 60:
        return '刚刚'
    elif 60*60 > timestamp >= 60:
        minutes = int(timestamp/60)
        return f"{minutes}分钟前"
    elif 60*60 >= timestamp < 60*60*24:
        hours = int(timestamp/60/60)
        return f"{hours}小时前"
    elif 60*60*24 >= timestamp > 60*60*24*30:
        days = int(timestamp/60/60/24)
        return f"{days}天前"
    else:
        return value.strftime("%Y/%m/%d %H:%M")
