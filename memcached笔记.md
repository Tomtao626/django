### telnet登录memcached
    -- telnet 127.0.0.1[ip地址] 11211[端口号]
'memcached'存书数据的方式的键值对

##### 常用命令
1.'**set**':
    -- 在memcached中添加一个key->value,如果这个key之前已经存在过，那么就会被替换。否则就是添加。
基本语法:
    '''
    -- > set key 0[是否需要压缩] 60[过期时间] 7[字符的长度]
       > tomtao
       > STORED
    '''

2.'**get**':
    -- 从memcached中获取一个数据，根据'key'来获取
基本语法:
    '''
    -- > get username[key的名称]
    '''

3.'**add**':
    -- 给memcached添加一个键值对，如果memcached中之前已经存在了这个'key'，那么就添加失败，否则就添加成功。
基本语法:
    '''
    -- > add username[key的名称] 0[是否需要压缩] 60[过期时间] 7[字符串的长度]
       > tomtao
       > STORED
       如果这个'key'已经存在，就会提示NOT STORED
    '''

4.'**delete**':
    -- 删除一个key及对应的value
基本语法:
    '''
    -- > delete username[key的名称]
    '''
    'flush_all'  删除memcached中所有的数据

5.'**stats**'
    -- 查看memcached的状态

6.'**incr**'
    -- 给一个值为**数字类型**的key的值加操作
基本语法:
    '''
       > set age 0 60 2
       > 20
       > STORED
    -- > get age
       > 20
       > incr age 10[要加的数值]
       > get age
       > 30
    '''

7.'**decr**'
    -- 给一个值为**数字类型**的key的值减操作
基本语法:
    '''
       > set age 0 60 2
       > 20
       > STORED
    -- > get age
       > 20
       > decr age 10[要减的数值]
       > get age
       > 10
    '''
telnet 默认最大的连接数是1024