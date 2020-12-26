1.values：用来指定在提取数据出来，需要提取哪些字段。默认情况下会把表中所有的字段全部都提取出来，可以使用values来进行指定，并且使用了values方法后，提取出的QuerySet中的数据类型不是模型，而是在values方法中指定的字段和值形成的字典：

 articles = Article.objects.values("title",'content')
 for article in articles:
     print(article)
以上打印出来的article是类似于{"title":"abc","content":"xxx"}的形式。
如果在values中没有传递任何参数，那么将会返回这个恶模型中所有的属性。

2.values_list：类似于values。只不过返回的QuerySet中，存储的不是字典，而是元组。示例代码如下：

 articles = Article.objects.values_list("id","title")
 print(articles)
那么在打印articles后，结果为<QuerySet [(1,'abc'),(2,'xxx'),...]>等。
如果在values_list中只有一个字段。那么你可以传递flat=True来将结果扁平化。示例代码如下：

 articles1 = Article.objects.values_list("title")
 >> <QuerySet [("abc",),("xxx",),...]>
 articles2 = Article.objects.values_list("title",flat=True)
 >> <QuerySet ["abc",'xxx',...]>
all：获取这个ORM模型的QuerySet对象。

3.select_related：在提取某个模型的数据的同时，也提前将相关联的数据提取出来。
比如提取文章数据，可以使用select_related将author信息提取出来，
以后再次使用article.author的时候就不需要再次去访问数据库了。
可以减少数据库查询的次数。示例代码如下：

 article = Article.objects.get(pk=1)
 >> article.author # 重新执行一次查询语句
 article = Article.objects.select_related("author").get(pk=2)
 >> article.author # 不需要重新执行查询语句了
select_related只能用在一对多或者一对一中，不能用在多对多或者多对一中。比如可以提前获取文章的作者，但是不能通过作者获取这个作者的文章，或者是通过某篇文章获取这个文章所有的标签。
 
4.prefetch_related：这个方法类似于select_related，也是用来在查询语句的时候，提前将指定的数据查询出来。
只不过这个方法是用来解决多对多和多对一得情况，这个方法会产生两个查询语句，所以如果在这个方法中，查询使用外键关联得
模型时，也会产生两个查询语句，因此如果查询的是外键关联得模型，建议使用select_related方法，
在查询多对多和多对一得关联得对象时，你在使用模型怎么访问这个多对多，那么就在这个方法中传递什么字符串，
比如想要获取图书的所有订单，示例代码如下：
    '''python
    #books = Book.objects.prefetch_related("bookorder_set")
    '''
需要注意的是，在使用prefetch_related查找出来的bookorder_set，建议不要再对其进行任何操作，比如filter，
不然又会产生N个查询语句。比如以下代码是不对的：
    '''python
    # books = Book.objects.prefetch_related("bookorder_set")
    # for book in books:
    #     print("*"*30)
    #     print(book.name)
    # 这个地方 如果对bookorder_set继续宁了操作，就会产生新的sql语句
    #     for order in book.bookorder_set.filter(price__gte=90):
    #         print(order.id)
    '''
如果确实需要使用预先查找的集合进行操作，则可以使用django.db.models.Prefetch来完成，示例代码如下：
    from django.db.models import Prefetch
    prefetch = Prefetch('bookorder_set', queryset=BookOrder.objects.filter(price__gte=90))
    books = Book.objects.prefetch_related(prefetch)
    for book in books:
        print(book.name)
        orders = book.bookorder_set.all()
        for order in orders:
            print(order.id)

5.defer和only
以上两个方法都会返回一个queryset对象，并且这个Queryset中装的都是模型，而不是字典
defer 查询某个模型时，过滤某些字段，在使用defer已经过滤了某个字段时，如果后面还需要使用这个字段，会重新发起一次查询操作，需谨慎操作 ，
only 查询某个模型时，只提取某些字段，在使用only时，未提取的字段，如果后面还需要使用，会重新发起一次查询操作，需谨慎操作 ，


6.get：获取满足条件的数据。这个函数只能返回一条数据，并且如果给的条件有多条数据，那么这个方法会抛出MultipleObjectsReturned错误，如果给的条件没有任何数据，那么就会抛出DoesNotExit错误。所以这个方法在获取数据的只能，只能有且只有一条。

7.create：创建一条数据，并且保存到数据库中。这个方法相当于先用指定的模型创建一个对象，然后再调用这个对象的save方法。示例代码如下：

article = Article(title='abc')
article.save()

# 下面这行代码相当于以上两行代码
article = Article.objects.create(title='abc')
8.get_or_create：根据某个条件进行查找，如果找到了那么就返回这条数据，如果没有查找到，那么就创建一个。示例代码如下：

obj,created= Category.objects.get_or_create(title='默认分类')
如果有标题等于默认分类的分类，那么就会查找出来，如果没有，则会创建并且存储到数据库中。
这个方法的返回值是一个元组，元组的第一个参数obj是这个对象，第二个参数created代表是否创建的。

9.bulk_create：一次性创建多个数据。示例代码如下：

Tag.objects.bulk_create([
    Tag(name='111'),
    Tag(name='222'),
])
10.count：获取提取的数据的个数。如果想要知道总共有多少条数据，那么建议使用count，而不是使用len(articles)这种。因为count在底层是使用select count(*)来实现的，这种方式比使用len函数更加的高效。

11.first和last：返回QuerySet中的第一条和最后一条数据。

12.aggregate：使用聚合函数。

13.exists：判断某个条件的数据是否存在。如果要判断某个条件的元素是否存在，那么建议使用exists，这比使用count或者直接判断QuerySet更有效得多。示例代码如下：

if Article.objects.filter(title__contains='hello').exists():
    print(True)
比使用count更高效：
if Article.objects.filter(title__contains='hello').count() > 0:
    print(True)
也比直接判断QuerySet更高效：
if Article.objects.filter(title__contains='hello'):
    print(True)
14.distinct：去除掉那些重复的数据。这个方法如果底层数据库用的是MySQL，那么不能传递任何的参数。比如想要提取所有销售的价格超过80元的图书，并且删掉那些重复的，那么可以使用distinct来帮我们实现，示例代码如下：

books = Book.objects.filter(bookorder__price__gte=80).distinct()
需要注意的是，如果在distinct之前使用了order_by，那么因为order_by会提取order_by中指定的字段，因此再使用distinct就会根据多个字段来进行唯一化，所以就不会把那些重复的数据删掉。示例代码如下：

orders = BookOrder.objects.order_by("create_time").values("book_id").distinct()
那么以上代码因为使用了order_by，即使使用了distinct，也会把重复的book_id提取出来。

15.update：执行更新操作，在SQL底层走的也是update命令。比如要将所有category为空的article的article字段都更新为默认的分类。示例代码如下：

Article.objects.filter(category__isnull=True).update(category_id=3)
注意这个方法走的是更新的逻辑。所以更新完成后保存到数据库中不会执行save方法，因此不会更新auto_now设置的字段。

16.delete：删除所有满足条件的数据。删除数据的时候，要注意on_delete指定的处理方式。

17.切片操作：有时候我们查找数据，有可能只需要其中的一部分。那么这时候可以使用切片操作来帮我们完成。QuerySet使用切片操作就跟列表使用切片操作是一样的。示例代码如下：

books = Book.objects.all()[1:3]
for book in books:
    print(book)
切片操作并不是把所有数据从数据库中提取出来再做切片操作。而是在数据库层面使用LIMIE和OFFSET来帮我们完成。所以如果只需要取其中一部分的数据的时候，建议大家使用切片操作。