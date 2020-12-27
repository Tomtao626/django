from django.db import models

# Create your models here.


class User(models.Model):
    """用户"""
    username = models.CharField(max_length=100)
