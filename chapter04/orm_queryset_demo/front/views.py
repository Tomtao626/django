from django.db import connection
from django.db.models import Q, F, Count, Prefetch
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from front.models import Book, BookOrder, Publisher, Author
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


def index7(request):
    # books = Book.objects.all()
    # books = Book.objects.prefetch_related("bookorder_set")
    # for book in books:
    #     print("*"*30)
    #     print(book.name)
    #     for order in book.bookorder_set.all():
    #         print(order.id)
    # books = Book.objects.prefetch_related("author")
    # for book in books:
    #     print(book.author.name)
    prefetch = Prefetch("bookorder_set", queryset=BookOrder.objects.filter(price__gte=90))
    books = Book.objects.prefetch_related(prefetch)
    for book in books:
        print(book.name)
        orders = book.bookorder_set.all()
        for order in orders:
            print(order.id)
    print(connection.queries)
    return HttpResponse("index7")


def index8(request):
    # defer 过滤掉某些字段
    # books = Book.objects.defer("name")
    # for book in books:
    #     print(book.name)
    #     print(type(book))
    # 只展示某些字段
    books = Book.objects.only('name')
    for book in books:
        print(f"{book.id},{book.name}")
    print(connection.queries)
    return HttpResponse("index8")


def index9(request):
    # get() 有且只能查询一条符合条件的数据
    book = Book.objects.get(pk=1)
    print(book)
    print(connection.queries[4]['sql'])
    # SELECT `book`.`id`, `book`.`name`, `book`.`pages`, `book`.`price`, `book`.`rating`, `book`.`author_id`, `book`.`publisher_id` FROM `book` WHERE `book`.`id` = 1
    return HttpResponse("index9")


def index10(request):
    # publisher = Publisher(name='测试出版社')
    # publisher.save()
    # create() 创建一条数据 并保存到对应的数据库
    publisher = Publisher.objects.create(name='测试出版社')
    publisher.save()
    print(connection.queries)
    return HttpResponse("index10")


def index11(request):
    # get_or_create() 获取一条符合的数据，没有则创建一条
    # result = Publisher.objects.get_or_create(name='测试666出版社')
    # print(result[0])
    # bulk_create() 创建多条数据
    publishe = Publisher.objects.bulk_create(
        [Publisher(name='TEST1'),
         Publisher(name='TEST2')]
    )
    return HttpResponse("index11")


def index12(request):
    # books = Book.objects.all()
    # print(len(books))
    # # count() 统计数量
    # books_count = Book.objects.count()
    # print(books_count)
    result = Book.objects.filter(name='红楼梦').exists()
    print(result)
    print(connection.queries)
    return HttpResponse("index12")


def index13(request):
    # distinct() 去重
    books = Book.objects.annotate(order_price=F('bookorder__price')).filter(bookorder__price__gte=90).distinct()
    for book in books:
        print(book)
    print(connection.queries)
    return HttpResponse("index13")


def index14(request):
    # update()
    # 所有的图书价格加5
    Book.objects.update(price=F('price')+5)
    # 等价于
    books = Book.objects.all()
    for book in books:
        book.price += 5
        book.save()
    return HttpResponse("index14")


def index15(request):
    Author.objects.filter(id__gte=2).delete()
    print(connection.queries)
    return HttpResponse("index15")


def index16(request):
    # 切片操作 只针对queryset对象生效
    publishers = Publisher.objects.get_queryset()[1:3]  # 取出下标1到2的数据 顾头不顾尾
    for publisher in publishers:
        print(publisher)
    print(connection.queries)
    return HttpResponse("index16")


def index17(request):
    # 什么时候Django会将QuerySet转换为SQL去执行：
    # 生成一个QuerySet对象并不会马上转换为SQL语句去执行。
    # 比如我们获取Book表下所有的图书：
    #
    # books = Book.objects.all()
    # print(connection.queries)
    # 我们可以看到在打印connection.quries的时候打印的是一个空的列表。说明上面的QuerySet并没有真正的执行。
    # 在以下情况下QuerySet会被转换为SQL语句执行：
    # 迭代：在遍历QuerySet对象的时候，会首先先执行这个SQL语句，然后再把这个结果返回进行迭代。比如以下代码就会转换为SQL语句：
    for book in Book.objects.all():
        print(book)
    # 使用步长做切片操作：QuerySet可以类似于列表一样做切片操作。做切片操作本身不会执行SQL语句，但是如果如果在做切片操作的时候提供了步长，那么就会立马执行SQL语句。需要注意的是，做切片后不能再执行filter方法，否则会报错。
    books = Book.objects.all()[0:2:2]
    # 调用len函数：调用len函数用来获取QuerySet中总共有多少条数据也会执行SQL语句。
    print(len(books))
    # 调用list函数：调用list函数用来将一个QuerySet对象转换为list对象也会立马执行SQL语句。
    book_ls = list(books)
    print(book_ls)
    # 判断：如果对某个QuerySet进行判断，也会立马执行SQL语句。
    if books:
        print(True)
    print(connection.queries)
    return HttpResponse("index17")