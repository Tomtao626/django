from django.db import models

# Create your models here.
from django.utils.timezone import now


class Article(models.Model):
    """article"""
    # primary_key=True 自定义某个字段为主键
    id = models.BigAutoField(primary_key=True)
    # is_removed = models.BooleanField(default=False)
    # 如果想要使用可以为null的BooleanField，应该使用NullBolleanField
    is_removed = models.NullBooleanField()
    # CharField如果是超过了254个字符，不建议使用
    # 推荐使用TextField：longtext
    title = models.CharField(max_length=200, default="")
    # auto_now_add 是在第一次添加数据进去的时候会自动获取当前的时间
    # auto_now 每次这个对象调用save方式时，才会更新获取当前时间
    create_time = models.DateTimeField(auto_now=True)
    signature = models.TextField()


class Person(models.Model):
    email = models.EmailField()
    signature = models.TextField(default="")


class Author(models.Model):
    username = models.CharField(max_length=100, null=True)
    age = models.IntegerField(null=True, db_column="author_age", default=0)
    create_time = models.DateTimeField(auto_now=True)
    tel = models.CharField(max_length=11, null=True, unique=True)

    def __str__(self):
        return f"<(Author id:{self.id},create_time:{self.create_time})>"

    class Meta:
        db_table = "author"
        ordering = ['-create_time', 'id']


