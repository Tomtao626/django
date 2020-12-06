from django.db import models


# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()

    def __str__(self):
        return f"<Article:id:{self.id},title:{self.title},content:{self.content}>"

    class Meta:
        db_table = 'article'
