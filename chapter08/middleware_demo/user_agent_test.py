# -*- coding: utf-8 -*-
"""
@Time:2021/1/14 23:37
@Auth:Canna
@File:user_agent_test.py
@IDE:PyCharm
@Motto:626(Always Be Coding)
"""

import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36'
}

resp = requests.get(url='http://127.0.0.1', headers=headers)
print(resp.text)
