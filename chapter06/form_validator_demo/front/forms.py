# -*- coding: utf-8 -*-
# @Time : 03/01/2021 15:57
# @Author : tomtao
# @Email : tp320670258@gmail.com
# @File : forms.py
# @Project : form_validator_demo

from django import forms
from django.core import validators
from django.views.generic import View

from front.models import User


class BaseForm(forms.Form):
    # 提取错误信息
    def get_errors(self):
        errors = self.errors.get_json_data()
        new_errors = dict()
        for key, error_dicts in errors.items():
            messages = list()
            for message in error_dicts:
                messages.append(message['message'])
            new_errors[key] = messages
        return new_errors


class MyForm(BaseForm):
    # email = forms.EmailField(error_messages={'invalid': '请输入正确的邮箱'})
    # price = forms.FloatField(error_messages={'invalid': '请输入浮点类型的数据'})
    # person_website = forms.URLField(error_messages={'invalid': '请输入合法的网址', 'required':'请输入一个网址'})
    # email = forms.CharField(validators=[validators.EmailValidator(message='请输入正确的邮箱地址')])
    telephone = forms.CharField(validators=[validators.RegexValidator(r'1[345678]\d(9)',
                                                                      message='请输入一个合法的手机号')])


class RegisterForm(BaseForm):
    username = forms.CharField(max_length=100)
    telephone = forms.CharField(validators=[validators.RegexValidator(r'1[345678]\d(9)',
                                                                      message='请输入一个合法的手机号')])
    pwd1 = forms.CharField(max_length=20, min_length=6)
    pwd2 = forms.CharField(max_length=20, min_length=6)

    # 自定义验证器
    def clean_telephone(self):
        telephone = self.cleaned_data.get('telephone')
        exists = User.objects.filter(telephone=telephone).exists()
        if exists:
            raise forms.ValidationError(message=f'{telephone}已被注册')
        return telephone


    # 验证多个字段 就需要重写clean方法
    def clean(self):
        cleaned_data = super().clean()
        pwd1 = cleaned_data.get('pwd1')
        pwd2 = cleaned_data.get('pwd2')
        if pwd1 != pwd2:
            raise forms.ValidationError(message='两次密码输入不一致')
        return cleaned_data