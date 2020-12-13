from datetime import datetime, time

from django.shortcuts import render
from django.http import HttpResponse
from .models import Article, Category
from django.utils.timezone import make_aware


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
    #  SELECT `article`.`id`, `article`.`title`, `article`.`content` FROM `article` WHERE `article`.`title` LIKE test1
    print(article_)
    #  <QuerySet [<Article: <Article:id:1,title:test1,content:test1111>>]>
    return HttpResponse("successfully")


def index1(request):
    result = Article.objects.filter(title__contains='test')
    print(result.query)
    #  对应sql语句
    #  SELECT `article`.`id`, `article`.`title`, `article`.`content` FROM `article` WHERE `article`.`title` LIKE BINARY %test%
    print(result)
    #  <QuerySet [<Article: <Article:id:1,title:test1,content:test1111>>, <Article: <Article:id:2,title:test2,content:test2222>>]>
    return HttpResponse("successfully")


def index2(request):
    result = Article.objects.filter(title__icontains='test')
    print(result.query)
    #  对应sql语句
    #  SELECT `article`.`id`, `article`.`title`, `article`.`content` FROM `article` WHERE `article`.`title` LIKE %test%
    print(result)
    #  <QuerySet [<Article: <Article:id:1,title:test1,content:test1111>>, <Article: <Article:id:2,title:test2,content:test2222>>]>
    return HttpResponse("successfully")


def index3(request):
    # articles = Article.objects.filter(id__in=[1,2,3])
    # for article in articles:
    #     print(article)
    # 获取id为1，2，3的文章的分类
    # categorys = Category.objects.filter(articles__id__in=[1,2,3])
    # 等价于 categorys = Category.objects.filter(article__in=[1,2,3])
    # 默认使用主键 id来进行查找
    """
        因为查询的字段是表的主键，故是可以查询的 article__in等价于 article__id__in
        如果要判断相关联表的字段，那么也是通过'__'来连接，并且在做关联查询的时候，不需要写'models_set'，
        直接使用模型的名字的小写化就可以了，比如通过分类去查找相应的文章，那么也可以通过'article__id__in'来连接。
        而不用写成'article_set__id__in'的形式,当然如果不想使用默认的形式，则可以使设置参数relative_query_name时，
        指定反向引用的名字
        示例代码如下:
        # 定义models
        class Category(models.Model):
            name = models.CharField(max_length=100, default='')
        
            class Meta:
                db_table = 'category'
                
        class Article(models.Model):
            title = models.CharField(max_length=200)
            content = models.TextField()
            category = models.ForeignKey("Category", null=True, on_delete=models.CASCADE,
                                         related_query_name='articles')
        # views操作
        category = Category.objects.filter(articles__id__in=[1,2,3])
        因为在category的ForeignKey中指定了relative_query_name为articles，
        所以不能使用article来进行反向查询了，这时候就需要使用articles__id__in来查询了
    """
    # for category in categorys:
    #     print(category)
    articles = Article.objects.filter(title__icontains='hello')
    categories = Category.objects.filter(articles__in=articles)
    for cateory in categories:
        print(cateory)
    print(categories.query)
    # 反向查询是将模型名字小写化 如'article__in'
    # 反向引用是将模型名字小写化 然后再加上'_set' 如 'article_set'
    # 二者都可以通过relative_query_name来指定自己的方式，而不使用默认的方式
    return HttpResponse("success!")


def index4(request):
    """
    查找id>2的所有文章
    gt ----> greater than 大于
    gte ---> greater than equal  大于等于
    lt ----> lower than  小于
    lte ---> lower than equal  小于等于
    :param request:
    :return:
    """
    articles = Article.objects.filter(id__gt=2)
    for article in articles:
        print(article)
    print(articles.query)
    return HttpResponse("successs")


def index5(request):
    # __startswith 以什么开头 区分大小写  __istartswith 以什么开头 不区分大小写
    # articles = Article.objects.filter(title__startswith='hello')
    # print(articles.query)
    # print(articles)
    # __endswith 以什么结尾 区分大小写  __iendswith 以什么结尾 不区分大小写
    articles = Article.objects.filter(title__endswith='hello')
    print(articles.query)
    print(articles)
    return HttpResponse('success')


def index6(request):
    # start_time = make_aware(datetime(year=2020, month=12, day=13, hour=23, minute=4, second=10))
    # end_time = make_aware(datetime(year=2020, month=12, day=13, hour=23, minute=30, second=10))
    # articles = Article.objects.filter(create_time__range=(start_time,end_time))
    # print(articles.query)
    # print(articles)
    """
    range 可以指定一个时间段 并且时间应该标记为'aware'时间，不然django会报警告
    需要使用make_aware()来避免这种警告
    """
    return HttpResponse("success")


def index7(request):
    """时间匹配"""
    # articles = Article.objects.filter(create_time__date=datetime(year=2020, month=12, day=13))
    # articles = Article.objects.filter(create_time__year=2020)
    # articles = Article.objects.filter(create_time__day=13)
    # 根据星期来查找 1表示星期日 7表示星期六 2-6表示星期一到星期五
    # articles = Article.objects.filter(create_time__week_day=1)
    start_time = time(hour=23, minute=12, second=56)
    end_time = time(hour=23, minute=12, second=57)
    # 根据时分秒查找 一般根据区间来查找
    articles = Article.objects.filter(create_time__time__range=(start_time, end_time))
    print(articles.query)
    print(articles)
    return HttpResponse("success")


def index8(request):
    # 判断某个字段是否为null
    # articles = Article.objects.filter(create_time__isnull=True)
    # articles = Article.objects.filter(title__regex=r"^hello")  # 区分大小写
    articles = Article.objects.filter(title__iregex=r"^hello")  # 不区分大小写
    print(articles.query)
    print(articles)
    return HttpResponse("success")
