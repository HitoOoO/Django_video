#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author  : Ch1ps8oy
# @Time    : 2022/2/21 17:42
# @FileName: comment.py
# @Software: PyCharm

from django.views.generic import View
from app.libs.base_render import render_to_response
from django.shortcuts import redirect,reverse
from django.http import JsonResponse
from app.models import Comment,ClientUser,Video

class CommentView(View):
    def post(self,request):
        content = request.POST.get('content','')
        user_id = request.POST.get('userId','')
        video_id = request.POST.get('videoId','')

        if not all([content,user_id,video_id]):
            return JsonResponse({'code':-1,'msg':'缺少必要字段'})

        print(content,user_id,video_id)
        video = Video.objects.get(pk=video_id)
        user = ClientUser.objects.get(pk=user_id)
        comment=Comment.objects.create(content=content,video=video,user=user)

        data = {'Comment':comment.data()}



        return JsonResponse({'code':0,'msg':'success','data':data})