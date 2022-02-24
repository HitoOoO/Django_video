#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author  : Ch1ps8oy
# @Time    : 2022/2/13 14:36
# @FileName: permission.py
# @Software: PyCharm

import functools
from django.shortcuts import redirect,reverse
from .consts import COOKIE_NAME
from app.models import ClientUser
def dashboard_auth(func):
    @functools.wraps(func)
    def wrapper(self,request,*args,**kwargs):
        user = request.user
        if not user.is_authenticated or not user.is_superuser:
            return redirect('{}?to={}'.format(reverse('login'),request.path))

        return func(self,request,*args,**kwargs)
    return wrapper


def client_auth(request):

    value = request.COOKIES.get(COOKIE_NAME)
    if not value:
        return None

    user = ClientUser.objects.filter(pk=value)

    if user and user.status:
        return user[0]
    else:
        return None