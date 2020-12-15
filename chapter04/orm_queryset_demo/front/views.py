from django.db import connection
from django.db.models import Q, F, Count
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from front.models import Book, BookOrder
from django.db.models.manager import Manager


def index(request):
    print(type(Book.objects))  # 所有方法都来源于QuerySet类
    return HttpResponse("successfully")


def index2(request):
    # 链式调用
    # id>2 且 id!=3
    # books = Book.objects.filter(id__gte=2).filter(~Q(id=3))
    # 等价于
    # books = Book.objects.filter(id__gte=2).exclude(id=3)
    # for book in books:
    #     print(book.name)
    # 使用annotate 新增参数
    books = Book.objects.annotate(author_name=F("author__name"))
    for book in books:
        # book.author_name 等价于 book.author.name 但后者增加了查询次数 影响性能
        print(book.name, book.author_name)
    print(connection.queries)
    return HttpResponse("successfully")


def index3(request):
    # 根据create_time从小到大排序
    # orders = BookOrder.objects.order_by("create_time")
    # 根据create_time从大到小排序
    # orders = BookOrder.objects.order_by("-create_time")
    # 首先根据时间从小到大排序，若时间相同，再根据价格从小到大排序
    # orders = BookOrder.objects.order_by("create_time", "price")
    # 根据订单的图书对应的评分从大到小排序
    # orders = BookOrder.objects.order_by("-book__rating")
    # for order in orders:
    #     print(f"{order.id}-{order.book.name}-{order.book.rating}")
    # orders = BookOrder.objects.all()  # 由于在model中已经指定了排序规则 所以不需要使用order_by了
    books = Book.objects.annotate(order_nums=Count("bookorder")).order_by("-order_nums")
    for book in books:
        print(book.name, book.order_nums)
    return HttpResponse("sucessfully")
