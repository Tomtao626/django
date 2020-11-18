from django.shortcuts import render,redirect,reverse
from django.db import connection


# Create your views here.
def get_cursor():
    return connection.cursor()


def index(request):
    cursor = get_cursor()
    cursor.execute("select id, name, author from book;")
    books = cursor.fetchall()
    return render(request, 'index.html', context={'books': books})


def add_book(request):
    if request.method == "GET":
        return render(request, 'add_book.html')
    else:
        name = request.POST.get("name")
        author = request.POST.get("author")
        cursor = get_cursor()
        cursor.execute(f"insert into book(id,name,author) value(2,'%s','%s')"%(name,author))
        return redirect(reverse('index'))


def book_detail(request, book_id):
    cursor = get_cursor()
    cursor.execute(f"select id,name,author from book where id={book_id}")
    book = cursor.fetchone()
    return render(request, 'book_detail.html', context={"book": book})


def book_del(request):
    if request.method == "POST":
        book_id = request.POST.get('book_id')
        cursor = get_cursor()
        cursor.execute(f"delete from book where id={book_id}")
        return redirect(reverse('index'))
    else:
        raise RuntimeError("删除图书的methos错误")