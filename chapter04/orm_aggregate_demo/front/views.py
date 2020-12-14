from django.db import connection
from django.db.models import Avg, Count, Max, Min, Sum
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
from front.models import Book, Author, BookOrder


def index(request):
    """获取所有图书的平均价格"""
    result = Book.objects.aggregate(Avg("price"))
    # 设置别名 avg=Avg("price")
    # 默认名称是 filed+__+聚合函数名称  如 price_avg
    print(result)
    # {'price__avg': 97.25}
    print(connection.queries)
    # 'SELECT AVG(`book`.`price`) AS `price__avg` FROM `book`
    # aggregate方法返回的是一个字典 而不是一个QuerySet对象 ，这个字典的key就是聚合函数的名字 值就是聚合函数执行后的结果
    return HttpResponse("successfully")


def index2(request):
    """获取每一本图书的销售价格"""
    books = Book.objects.annotate(avg=Avg("bookorder__price"))
    for book in books:
        print(f"{book.name}/{book.avg}")
    print(connection.queries)
    return HttpResponse("succesfully")


def index3(request):
    """book表总共有多少本书"""
    # result = Book.objects.aggregate(book_nums=Count("id"))
    # print(result)
    # print(connection.queries)
    # 要统计表中总共有多少个不同邮箱
    # result = Author.objects.aggregate(email_nums=Count("email", distinct=True))
    # print(result)
    # print(connection.queries)

    # annotate
    books = Book.objects.annotate(book_nums=Count("bookorder"))
    for book in books:
        print(f"{book.name}/{book.book_nums}")
    print(connection.queries)
    return HttpResponse("successfully")


def index4(request):
    """获取作者年龄的最大最小值"""
    # author = Author.objects.aggregate(max=Max("age"), min=Min("age"))
    # print(author)
    # print(connection.queries)
    # 获取每一本图书售卖时候的最大价格及最小价格


    books = Book.objects.annotate(max=Max("bookorder__price"), min=Min("bookorder__price"))
    for book in books:
        print(f"{book.name}/{book.max}/{book.min}")
    print(connection.queries)
    return HttpResponse("successfully")


def index5(request):
    """求所有图书的销售总额"""
    # result = BookOrder.objects.aggregate(total=Sum('price'))
    # print(result)
    # print(connection.queries)
    # 每一本图书的销售总额
    # books = Book.objects.annotate(total=Sum("bookorder__price"))
    # for book in books:
    #     print(f"{book.name}/{book.total}")
    # print(connection.queries)
    # 2020年度销售总额
    # result = BookOrder.objects.filter(create_time__year=2020).aggregate(total=Sum('price'))
    # print(result)
    # print(connection.queries)
    # 求每一本图书在2020年度的销售总额
    books = Book.objects.filter(bookorder__create_time__year=2020).annotate(total=Sum("bookorder__price"))
    for book in books:
        print(f"{book.name}/{book.total}")
    print(connection.queries)
    return HttpResponse("successfully")