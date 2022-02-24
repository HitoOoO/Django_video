#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author  : Ch1ps8oy
# @Time    : 2022/2/24 13:03
# @FileName: comments.py
# @Software: PyCharm
from django.views.generic import View
from django.shortcuts import redirect,reverse
from app.models import Comment
from django.http import JsonResponse

class Comments(View):

    def get(self,request,comment_id,video_id):
        comment = Comment.objects.get(pk=comment_id)

        comment.status = not comment.status
        comment.save()

        return redirect(reverse('video_sub',kwargs={'video_id' : video_id }))

