from django.db import models


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100, default='')

    class Meta:
        db_table = 'category'


class Article(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    category = models.ForeignKey("Category", null=True, on_delete=models.CASCADE,
                                 related_query_name='articles')
    create_time = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return f"<Article:id:{self.id},title:{self.title},content:{self.content}>"

    class Meta:
        db_table = 'article'
