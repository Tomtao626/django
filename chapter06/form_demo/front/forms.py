# -*- coding: utf-8 -*-
# @Time : 03/01/2021 15:32
# @Author : tomtao
# @Email : tp320670258@gmail.com
# @File : forms.py
# @Project : form_demo

from django import forms


class MessageBoardForm(forms.Form):
    title = forms.CharField(max_length=100, min_length=2, label='标题',
                            error_messages=dict(min_length='最小不能小于一个字符'))
    content = forms.CharField(widget=forms.Textarea, label='内容',
                              error_messages=dict(required='必须要传content字段'))
    email = forms.EmailField(label='邮箱', error_messages=dict(required='必须要传email字段'))
    reply = forms.BooleanField(required=False, label='是否回复')
