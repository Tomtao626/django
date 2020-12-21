随着项目越来越大，采用写原生SQL的方式在代码中会出现大量的SQL语句，那么问题就出现了：

SQL语句重复利用率不高，越复杂的SQL语句条件越多，代码越长。会出现很多相近的SQL语句。
很多SQL语句是在业务逻辑中拼出来的，如果有数据库需要更改，就要去修改这些逻辑，这会很容易漏掉对某些SQL语句的修改。
写SQL时容易忽略web安全问题，给未来造成隐患。SQL注入。
ORM，全称Object Relational Mapping，中文叫做对象关系映射，通过ORM我们可以通过类的方式去操作数据库，而不用再写原生的SQL语句。通过把表映射成类，把行作实例，把字段作为属性，ORM在执行对象操作的时候最终还是会把对应的操作转换为数据库原生语句。使用ORM有许多优点：

易用性：使用ORM做数据库的开发可以有效的减少重复SQL语句的概率，写出来的模型也更加直观、清晰。
性能损耗小：ORM转换成底层数据库操作指令确实会有一些开销。但从实际的情况来看，这种性能损耗很少（不足5%），只要不是对性能有严苛的要求，综合考虑开发效率、代码的阅读性，带来的好处要远远大于性能损耗，而且项目越大作用越明显。
设计灵活：可以轻松的写出复杂的查询。
可移植性：Django封装了底层的数据库实现，支持多个关系数据库引擎，包括流行的MySQL、PostgreSQL和SQLite。可以非常轻松的切换数据库。


创建ORM模型：
ORM模型一般都是放在app的models.py文件中。每个app都可以拥有自己的模型。并且如果这个模型想要映射到数据库中，那么这个app必须要放在settings.py的INSTALLED_APP中进行安装。以下是写一个简单的书籍ORM模型。示例代码如下：

from django.db import models
class Book(models.Model):
    name = models.CharField(max_length=20,null=False)
    author = models.CharField(max_length=20,null=False)
    pub_time = models.DateTimeField(default=datetime.now)
    price = models.FloatField(default=0)
以上便定义了一个模型。这个模型继承自django.db.models.Model，如果这个模型想要映射到数据库中，就必须继承自这个类。这个模型以后映射到数据库中，表名是模型名称的小写形式，为book。在这个表中，有四个字段，一个为name，这个字段是保存的是书的名称，是varchar类型，最长不能超过20个字符，并且不能为空。第二个字段是作者名字类型，同样也是varchar类型，长度不能超过20个。第三个是出版时间，数据类型是datetime类型，默认是保存这本书籍的时间。第五个是这本书的价格，是浮点类型。
还有一个字段我们没有写，就是主键id，在django中，如果一个模型没有定义主键，那么将会自动生成一个自动增长的int类型的主键，并且这个主键的名字就叫做id。

映射模型到数据库中：
将ORM模型映射到数据库中，总结起来就是以下几步：

在settings.py中，配置好DATABASES，做好数据库相关的配置。
在app中的models.py中定义好模型，这个模型必须继承自django.db.models。
将这个app添加到settings.py的INSTALLED_APP中。
在命令行终端，进入到项目所在的路径，然后执行命令python manage.py makemigrations来生成迁移脚本文件。
同样在命令行中，执行命令python manage.py migrate来将迁移脚本文件映射到数据库中。