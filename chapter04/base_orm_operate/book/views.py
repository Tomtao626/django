from django.shortcuts import render
from .models import Book
from django.http import HttpResponse

# Create your views here.

def index(request):
    """
    orm操作
    :param request:
    :return:
    """
    # orm新增数据
    '''
    book = Book()
    book.name = "西游记"
    book.author = "吴承恩"
    book.price = 888
    book.save()
    '''
    # orm查询数据
    # 2.1 根据主键进行查询
    # pk -- > primary key
    # Book.objects.get(pk=1) = Book.objects.get(id=1)
    '''
    book_one = Book.objects.get(pk=2)
    print(book_one)
    '''
    # 2.2 根据其他条件进行查找
    '''
    book_lists = Book.objects.filter(name = "西游记").first()
    print(book_lists)
    '''
    # 3 删除数据
    '''
    book = Book.objects.get(pk=1)
    book.delete()
    '''
    # 4 更新数据
    book = Book.objects.get(pk=2)
    book.price = 101
    book.save()
    return HttpResponse("图书添加成功!")