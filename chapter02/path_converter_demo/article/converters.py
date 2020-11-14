#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/5/26 23:47
# @Author : Tom_tao
# @Site : 
# @File : converters.py
# @Software: PyCharm

from django.urls import register_converter


class CategoryConverter(object):
    regex = r"\w+|(\w+\+\w+)+"

    def to_python(self,value):
        # python+django+flask
        # ['ptyhon','django','flask']
        result = value.split('+')
        return result

    def to_url(self,value):
        # value:['ptyhon','django','flask']
        # python+django+flask
        if isinstance(value,list):
            result = "+".join(value)
            return result
        else:
            return RuntimeError("转换url时错误，分类参数必须为列表")

register_converter(CategoryConverter,'cate')