# -*- coding: utf-8 -*-
# @Time : 2021/1/4 22:37
# @Author : tomtao
# @Email : tp320670258@gmail.com
# @File : forms.py
# @Project : modelform_demo
from django import forms
from .models import Book, User


class AddBookForm(forms.ModelForm):
    def clean_page(self):
        page = self.cleaned_data.get('page')
        if page < 100:
            raise forms.ValidationError('页数不能小于100页')
        return page

    class Meta:
        model = Book
        fields = "__all__"  # 全部字段
        # fields = ['title', 'page']  # 部分字段
        # exclude = ['price']  # 除开price的字段全部留下
        error_messages = {
            'page': {
                'required': '请传入page参数',
                'invalid': '请传入一个合法的page参数'
            },
            'title': {
                'max_length': 'title不能超过100个字符',
                'required': '请传入title参数',
                'invalid': '请传入一个合法的title参数'
            },
            'price': {
                'max_value': '图书价格不能超过1000元'
            }
        }


class RegisterForm(forms.ModelForm):
    pwd1 = forms.CharField(max_length=16, min_length=6)
    pwd2 = forms.CharField(max_length=16, min_length=6)

    def clean(self):
        cleaned_data = super().clean()
        pwd1 = cleaned_data.get('pwd1')
        pwd2 = cleaned_data.get('pwd2')
        if pwd1 != pwd2:
            raise forms.ValidationError('两次密码输入不一致')
        return cleaned_data

    class Meta:
        model = User
        exclude = ['password']
