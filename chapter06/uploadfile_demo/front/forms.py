# -*- coding: utf-8 -*-
# @Time : 2021/1/5 0:00
# @Author : tomtao
# @Email : tp320670258@gmail.com
# @File : forms.py
# @Project : uploadfile_demo
from django import forms
from .models import Article


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = "__all__"
        error_messages = {
            'thumbnail': {
                'invalid_image': '请上传正确格式的图片'
            }
        }
