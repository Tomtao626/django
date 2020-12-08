from django.shortcuts import render
from django.http import HttpResponse
from .models import Article


# Create your views here.

def index(request):
    """
    在windows操作系统上，mysql的排序规则（collation）无论是什么，都是大小写不敏感的
    在linux操作系统中，mysql的排序规则（collation）是utf8_bin，就是大小写敏感的
    :param request:
    :return:
    """
    # article = Article.objects.filter(id_exact=1)  # Queryset
    article = Article.objects.filter(title__exact="Test1")
    """
        article = Article.objects.filter(title__exact="Test1")
        article = Article.objects.filter(title__exact=None)
        等价于以下Isql语句
        SELECT `article`.`id`, `article`.`title`, `article`.`content` FROM `article` WHERE `article`.`title` = Test1;
        SELECT `article`.`id`, `article`.`title`, `article`.`content` FROM `article` WHERE `article`.`title` is NULL;
    """
    # title_exact 等价于title
    # 打印对应的sql语句
    print(article.query)
    # SELECT `article`.`id`, `article`.`title`, `article`.`content` FROM `article` WHERE `article`.`title` = Test1
    print(article)
    # < QuerySet[ < Article: < Article: id:1, title: test1, content: test1111 >>] >

    """
        exact和iexact 就是=和like的区别
    """
    article_ = Article.objects.filter(title__iexact='test1')
    print(article_.query)
    #  sql语句
    # SELECT `article`.`id`, `article`.`title`, `article`.`content` FROM `article` WHERE `article`.`title` LIKE test1
    print(article_)
    # <QuerySet [<Article: <Article:id:1,title:test1,content:test1111>>]>
    return HttpResponse("successfully")
