from django.db import models

# Create your models here.

class Book(models.Model):
    """
    图书
    """
    name = models.CharField(max_length=100, null=False)
    author = models.CharField(max_length=100, null=False)
    price = models.FloatField(default=0)

    def __str__(self):
        # <Book:(name,author,price)>
        return f"<Book:({self.name},{self.author},{self.price})>"
