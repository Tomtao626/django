# -*- coding: utf-8 -*-
"""
@Time:2021/1/11 21:49
@Auth:Canna
@File:main.py
@IDE:PyCharm
@Motto:626(Always Be Coding)
"""

import memcache


# 在连接前 先确认先启动memcached
mc = memcache.Client(["localhost:11211"], debug=True)

# mc.set("username", "tomtao", time=120)
# mc.set_multi(dict(title='红楼梦', content='hello world'), time=120)

# username = mc.get('username')
# print(username)
#
# mc.delete('username')
#
# username = mc.get('username')
# print(username)

mc.incr('count', delta=30)  # 加操作
print(mc.get('count'))

mc.incr('count', delta=30)  # 减操作
print(mc.get('count'))