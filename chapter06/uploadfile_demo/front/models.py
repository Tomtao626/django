from django.db import models
from django.core import validators


# Create your models here.


class Article(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    # thumbnail = models.FileField(upload_to='%Y/%m/%d', validators=[validators.FileExtensionValidator(['txt'], message='thumbnail必须为txt格式')])
    thumbnail = models.ImageField(upload_to='%Y/%m/%d')  # 依赖于pillow库 请安装pip install pillow

    class Meta:
        db_table = 'article'
        verbose_name = '文章'


