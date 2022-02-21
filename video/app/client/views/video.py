#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author  : Ch1ps8oy
# @Time    : 2022/2/20 17:14
# @FileName: video.py
# @Software: PyCharm

from django.views.generic import View
from app.libs.base_render import render_to_response
from app.models import Video
from app.model.video import FromType
from django.shortcuts import redirect,reverse,get_object_or_404
class ExVideo(View):
    TEMPLATE = 'client/video/video.html'

    def get(self,request):
        videos = Video.objects.exclude(from_to=FromType.custom.value)
        data = {'videos':videos}
        return render_to_response(request,self.TEMPLATE,data=data)

class CusVideo(View):
    TEMPLATE = 'client/video/video.html'

    def get(self, request):
        videos = Video.objects.filter(from_to=FromType.custom.value)
        data = {'videos': videos}
        return render_to_response(request, self.TEMPLATE, data=data)

class VideoSub(View):
    TEMPLATE = 'client/video/video_sub.html'

    def get(self,request,video_id):
        video = get_object_or_404(Video,pk=video_id)
        data = {'video':video }
        return render_to_response(request,self.TEMPLATE,data=data)

