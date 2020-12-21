查询条件
exact：
使用精确的=进行查找。如果提供的是一个None，那么在SQL层面就是被解释为NULL。示例代码如下：

article = Article.objects.get(id__exact=14)
article = Article.objects.get(id__exact=None)
以上的两个查找在翻译为SQL语句为如下：

select ... from article where id=14;
select ... from article where id IS NULL;
iexact：
使用like进行查找。示例代码如下：

article = Article.objects.filter(title__iexact='hello world')
那么以上的查询就等价于以下的SQL语句：

select ... from article where title like 'hello world';
注意上面这个sql语句，因为在MySQL中，没有一个叫做ilike的。所以exact和iexact的区别实际上就是LIKE和=的区别，在大部分collation=utf8_general_ci情况下都是一样的（collation是用来对字符串比较的）。

contains：
大小写敏感，判断某个字段是否包含了某个数据。示例代码如下：

articles = Article.objects.filter(title__contains='hello')
在翻译成SQL语句为如下：

select ... where title like binary '%hello%';
要注意的是，在使用contains的时候，翻译成的sql语句左右两边是有百分号的，意味着使用的是模糊查询。而exact翻译成sql语句左右两边是没有百分号的，意味着使用的是精确的查询。

icontains：
大小写不敏感的匹配查询。示例代码如下：

articles = Article.objects.filter(title__icontains='hello')
在翻译成SQL语句为如下：

select ... where title like '%hello%';


sql模糊查询
contains ----> like binary  大小写敏感
icontains ----> like   大小写不敏感


QuerySet.query  .query可以用来查看对应orm语句的sql语句 但是query只能用于QuerySet对象上，不能用在普通的orm模型上
如果是.get获取的数据，就无法使用.query来获取对应的sql语句，因为get返回的是ore模型，而不是QuerySet
如果是通过filter获取的数据，是可以用.query来获取对应的sql语句的