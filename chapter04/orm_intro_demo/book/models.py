from django.db import models

# Create your models here.

# 如果要将一个普通的类变成一个可以映射到数据库中的orm模型
# 那么必须要将父类设置为models.Model或者它的子类
class Book(models.Model):
    """
    图书
    id int 自增长
    name varchar(100)
    author varchar(100)
    price float
    """
    id = models.AutoField(primary_key=True, verbose_name='id')
    name = models.CharField(max_length=100, null=False, verbose_name='图书名称')
    author = models.CharField(max_length=100, null=False, verbose_name='作者')
    price = models.FloatField(null=True, default=0, verbose_name='价格')


class Publisher(models.Model):
    """
    出版社
    """
    name = models.CharField(max_length=100, null=False)
    address = models.CharField(max_length=100, null=False)

# 使用migrations生成迁移脚本文件
# python manage.py makemigrations

# 使用migrate将新生成的迁移脚本文件映射到数据库中
# python manage.py migrate
