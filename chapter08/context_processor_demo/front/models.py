from django.db import models

# Create your models here.


class User(models.Model):
    """用户"""
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=16)
    telephone = models.CharField(max_length=11)

    class Meta:
        db_table = 'user'
        verbose_name = '用户'
