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