#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author  : Ch1ps8oy
# @Time    : 2022/2/12 15:19
# @FileName: auth.py
# @Software: PyCharm
from django.views.generic import View
from app.libs.base_render import render_to_response
from django.shortcuts import redirect,reverse
from django.contrib.auth import login,authenticate,logout
from django.contrib.auth.models import User
from django.core.paginator import Paginator
from app.utils.permission import dashboard_auth
from app.models import ClientUser
from django.http import JsonResponse
class Login(View):
    TEMPLATE = 'dashboard/auth/login.html'

    def get(self,request):
        if request.user.is_authenticated:              #判断是否已经是登陆状态
            return redirect(reverse('dashboard_index'))

        to = request.GET.get('to','')
        data = {'error': '','to':to}
        return render_to_response(request,self.TEMPLATE,data=data)

    def post(self,request):
        username = request.POST.get('username')    #获取表单提交的用户名密码
        password = request.POST.get('password')
        to = request.GET.get('to','')

        data = {}
        print(username,password)

        exits = User.objects.filter(username=username).exists()  #判断用户是否存在
        data['error'] = '没有该用户'
        if not exits:
            return render_to_response(request,self.TEMPLATE,data=data)   #不存在报用户不存在的错误

        user = authenticate(username=username,password=password)  #验证用户

        if not user:
            data['error'] = '密码错误'
            return render_to_response(request,self.TEMPLATE,data=data)

        if not user.is_superuser:
            data['error'] = '你无权登录'
            return render_to_response(request,self.TEMPLATE,data=data)
        login(request,user)

        if to:
            return redirect(to)
        return redirect(reverse('dashboard_index'))

class Logout(View):
    def get(self,request):
        logout(request)
        return redirect(reverse('login'))



class AdminManger(View):

    TEMPLATE = 'dashboard/auth/admin.html'
    @dashboard_auth
    def get(self,request):
        users = User.objects.all()                      #显示全部用户
        page = request.GET.get('page',1)
        p  = Paginator(users,1)                         #默认一页显示两个
        total_page = p.num_pages
        if int(page) <=1:
            page = 1

        current_page = p.get_page(int(page)).object_list

        data = {'users': current_page,'total':total_page,'page_num':int(page)}
        return render_to_response(request,self.TEMPLATE,data=data)

class UpdateAdminStatus(View):
    def get(self,request):

        status = request.GET.get('status','on')         #获取用户状态

        _status = True if status == 'on' else False              #判断用户状态，点击添加删除 对应修改状态
        request.user.is_superuser = _status
        request.user.save()

        return redirect(reverse('admin_manger'))


class ClientManager(View):
    TEMPLATE ='dashboard/auth/client_user.html'

    def get(self,request):

        users= ClientUser.objects.all()
        data = {'users':users}
        return render_to_response(request,self.TEMPLATE,data=data)


    def post(self,request):
        user_id = request.POST.get('userId')

        user = ClientUser.objects.get(pk=user_id)
        user.update_status()
        return JsonResponse({'code':0,'msg':'success'})