#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author  : Ch1ps8oy
# @Time    : 2022/2/20 13:35
# @FileName: base.py
# @Software: PyCharm
from django.views.generic import View
from app.libs.base_render import render_to_response

class Index(View):
    TEMPLATE = 'client/base.html'
    def get(self,request):

        return render_to_response(request,self.TEMPLATE)