# -*- coding: utf-8 -*-
# @Time : 03/01/2021 15:57
# @Author : tomtao
# @Email : tp320670258@gmail.com
# @File : forms.py
# @Project : form_validator_demo

from django import forms


class MyForm(forms.Form):
    # email = forms.EmailField(error_messages={'invalid': '请输入正确的邮箱'})
    # price = forms.FloatField(error_messages={'invalid': '请输入浮点类型的数据'})
    person_website = forms.URLField(error_messages={'invalid': '请输入合法的网址', 'required':'请输入一个网址'})
