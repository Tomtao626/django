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


def index4(request):
    # 只查询特定的字段
    # books = Book.objects.values("id", "name", author_name=F("author__name"))
    # books是一个queryset对象
    # 如果想要当前模型关联的属性，查找顺序和filter一样 使用F表达式可实现关键字名字自定义
    # 自定义的名字不能和模型已有的字段名相同，
    # books = Book.objects.values("id", "name", order_nums=Count('bookorder'))
    # for book in books:
    #     print(book)
    # 返回字典
    # 在values 中 ，也可以使用聚合函数
    # values_list()
    # books = Book.objects.values_list('id', 'name')
    # for book in books:
    #     print(book)
    # 返回元组
    books = Book.objects.values_list('name', flat=True)
    for book in books:
        # 当只需要返回一个字段时，默认是返回一个元组(红楼梦,)
        # 如果需要返回一个字符串 红楼梦，可以使用flag参数 并设置为true即可
        print(book)
    return HttpResponse("successfully")


def index5(request):
    books = Book.objects.all()
    # all方法返回一个queryset对象
    print(type(books))
    for book in books:
        print(book.name)
    return HttpResponse("index5")


def index6(request):
    # books = Book.objects.all()
    # 只适合外键得关联对象上， 不适合多对多 和 多对一
    books = Book.objects.select_related("author", "publisher")
    for book in books:
        print(book.author.name)
        print(book.publisher.name)
    print(connection.queries)
    return HttpResponse("index6")