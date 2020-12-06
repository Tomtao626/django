from django.db import models

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=100)


class Article(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    category = models.ForeignKey("category", on_delete=models.CASCADE)
    author = models.ForeignKey("frontuser.FrontUser",
                               on_delete=models.CASCADE, null=True)


class Comment(models.Model):
    content = models.TextField()
    origin_comment = models.ForeignKey("self", on_delete=models.CASCADE)