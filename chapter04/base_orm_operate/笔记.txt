ORM操作

1.新增数据
book = Book()
book.name = '我有一个梦想'
book.author = 'lisa'
book.price = 9999
book.save()

2.删除数据
book = Book.objects.get(pk=1)
book.delete()

3.更新数据
book = Book.objects.get(pk=2)
book.price = 101
book.save()

4.查询数据
# 查一条
book_one = Book.objects.get(pk=1)
# 或者 book_one = Book.objects.get(pk=1).first()
# 查多条
books = Book.objects.all()
# 条件过滤
books = Book.objects.filter(name="三国演义")