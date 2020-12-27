from django.db import models

# Create your models here.


class Article(models.Model):
    """文章"""
    title = models.CharField(max_length=100)
    content = models.TextField(null=True)
    # create_time = models.DateTimeField(null=True)
