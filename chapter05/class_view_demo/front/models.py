from django.db import models

# Create your models here.


class Article(models.Model):
    """文章"""
    title = models.CharField(max_length=100)
    content = models.TextField()
    add_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'article'
