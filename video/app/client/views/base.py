#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author  : Ch1ps8oy
# @Time    : 2022/2/20 13:35
# @FileName: base.py
# @Software: PyCharm
from django.views.generic import View
from app.libs.base_render import render_to_response
from django.shortcuts import redirect,reverse

class Index(View):
    TEMPLATE = 'client/base.html'
    def get(self,request):

        return redirect(reverse('client_ex_video'))
