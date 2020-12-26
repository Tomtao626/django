from django.db import models

# Create your models here.


class Author(models.Model):
    """作者模型"""
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    email = models.EmailField()

    class Meta:
        db_table = 'author'


# def publisher_default_data():
#     return Publisher.objects.get_or_create(name='默认出版社')


# class Publisher(models.Model):
#     """出版社"""
#     name = models.CharField(max_length=300, default=publisher_default_data())
#
#     class Meta:
#         db_table = 'publisher'

class Publisher(models.Model):
    """出版社"""
    name = models.CharField(max_length=300)

    class Meta:
        db_table = 'publisher'


class Book(models.Model):
    """图书模型"""
    name = models.CharField(max_length=300)
    pages = models.IntegerField()
    price = models.FloatField()
    rating = models.FloatField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)

    class Meta:
        db_table = 'book'


class BookOrder(models.Model):
    """图书订单模型"""
    book = models.ForeignKey("Book", on_delete=models.CASCADE)
    price = models.FloatField()
    create_time = models.DateTimeField(auto_now_add=True, null=True)

    class Meta:
        db_table = 'book_order'
        # 指定排序规则
        ordering = ["-create_time", "price"]

