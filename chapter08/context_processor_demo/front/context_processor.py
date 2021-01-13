# -*- coding: utf-8 -*-
"""
@Time:2021/1/13 23:33
@Auth:Canna
@File:context_processor.py
@IDE:PyCharm
@Motto:626(Always Be Coding)
"""

from .models import User


def front_user(request):
    user_id = request.session.get('user_id')
    context = dict()
    if user_id:
        try:
            user = User.objects.get(pk=user_id)
            context.update(dict(front_user=user))
        except Exception as e:
            print(e)
    return context
