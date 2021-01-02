# -*- coding: utf-8 -*-
# @Time : 02/01/2021 16:14
# @Author : tomtao
# @Email : tp320670258@gmail.com
# @File : views.py
# @Project : httpsresponse_demo
import ujson
from django.http import HttpResponse, JsonResponse


def index(request):
    response = HttpResponse()
    response['content'] = "<h1>测试信息<h1>"
    response['Content-Type'] = 'text/plain;charset=utf-8'
    response['status_code'] = 500
    response['PASSWORD'] = 'yttttttt'
    return response


def jsonresponse_view(request):
    # person = dict(username='tomtao',passwd='324fdst45yfg',age=99,score=999)
    # 使用httpresponse返回json数据
    # json化处理
    # person_str = ujson.dumps(person)
    # response = HttpResponse(person_str, content_type='application/json')
    # 使用jsonresponse返回json数据
    # response = JsonResponse(person)
    # JsonResponse默认只能对字典进行dump，如果要对非字典数据进行dump，需要给JsonResponse传递一个safe=False参数
    person = [{'username': 'tomtao', 'passwd': '324fdst45yfg', 'age': 99, 'score': 999},
              {'username': 'tomtao1', 'passwd': '324fdst45yfreg', 'age': 999, 'score': 999}]
    response = JsonResponse(person, safe=False)
    return response
