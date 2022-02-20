#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author  : Ch1ps8oy
# @Time    : 2022/2/12 13:50
# @FileName: base.py
# @Software: PyCharm

from django.views.generic import View
from app.libs.base_render import render_to_response
from app.utils.permission import dashboard_auth

class Index(View):
    TEMPLATE = 'dashboard/index.html'
    @dashboard_auth
    def get(self,request):

        return render_to_response(request,self.TEMPLATE)