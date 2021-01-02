# -*- coding: utf-8 -*-
# @Time : 02/01/2021 16:49
# @Author : tomtao
# @Email : tp320670258@gmail.com
# @File : views.py
# @Project : generate_csv_demo
import csv

from django.http import HttpResponse, StreamingHttpResponse
from django.template import loader


def index(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = "attachment;filename=test.csv"
    writer = csv.writer(response)
    writer.writerow(['username', 'score'])
    writer.writerow(['testname', '999'])
    writer.writerow(['张三', '1249845'])
    return response


def template_csv_view(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = "attachment;filename=test.csv"
    context = {
        'rows': [
            ['username', 'score'],
            ['testname', 9999]
        ]
    }
    template = loader.get_template('test.txt')
    csv_template = template.render(context)
    response.content = csv_template
    return response


def large_csv_view(request):
    # 尽量少使用 超大文件建议使用
    # 使用StreamingHttpResponse处理大量数据的请求
    # response = StreamingHttpResponse(content_type='text/csv')
    # response['Content-Disposition'] = 'attachment;filename=large.csv'
    # rows = (f"Rows {row},{row}\n" for row in range(0, 1000000))
    # response.streaming_content = rows
    # return response
    # 使用HttpResponse处理大量数据的请求
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment;filename=large.csv'
    writer = csv.writer(response)
    for row in range(0, 1000000):
        writer.writerow([f'Row {row}', f'Row {row}'])
    return response
