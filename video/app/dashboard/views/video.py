#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author  : Ch1ps8oy
# @Time    : 2022/2/13 17:03
# @FileName: video.py
# @Software: PyCharm

from django.views.generic import View
from django.shortcuts import redirect,reverse
from django.core.paginator import Paginator
from app.utils.permission import dashboard_auth
from app.libs.base_render import render_to_response
from app.utils.common import check_and_get_video_type
from app.model.video import (VideoType,FromType,NationalityType,
                             Video,VideoSub,IdentityType,VideoStar)


class ExternaVideo(View):
    TEMPLATE = 'dashboard/video/externa_video.html'

    @dashboard_auth
    def get(self,request):
        error = request.GET.get('error','')
        data = {'error':error}
        videos = Video.objects.exclude(from_to=FromType.custom.value)
        data['videos'] = videos
        return render_to_response(request,self.TEMPLATE,data=data)


    def post(self,request):
        name = request.POST.get('name')
        image = request.POST.get('image')
        video_type = request.POST.get('video_type')
        from_to = request.POST.get('from_to')
        nationality = request.POST.get('nationality')
        info = request.POST.get('info')

        if not all([name,image,video_type,from_to,nationality,info]):
            return redirect('{}?error={}'.format(reverse('externa_video'),'缺少必要字段'))

        result = check_and_get_video_type(VideoType,video_type,'非法视频类型')
        if result.get('code') != 0:
            return redirect('{}?error={}'.format(reverse('externa_video'),result['msg']))


        result = check_and_get_video_type(FromType,from_to,'非法的来源')
        if result.get('code') != 0:
            return redirect('{}?error={}'.format(reverse('externa_video'),result['msg']))


        result = check_and_get_video_type(NationalityType,nationality,'非法的国籍')
        if result.get('code') != 0:
            return redirect('{}?error={}'.format(reverse('externa_video'),result['msg']))


        Video.objects.create(
            name=name,
            image=image,
            video_type=video_type,
            from_to=from_to,
            nationality=nationality,
            info=info
        )
        return redirect(reverse('externa_video'))

class VideoSubView(View):
    TEMPLATE = 'dashboard/video/video_sub.html'

    @dashboard_auth
    def get(self,request,video_id):
        data = {}
        video = Video.objects.get(pk=video_id)
        error = request.GET.get('error','')
        data['video'] = video
        data['error'] = error

        return render_to_response(request,self.TEMPLATE,data=data)

    def post(self,request,video_id):
        url = request.POST.get('url')

        video = Video.objects.get(pk=video_id)
        length = video.video_sub.count()


        VideoSub.objects.create(video=video,url=url,number=length + 1)

        return redirect(reverse('video_sub',kwargs={'video_id':video_id}))


class VideoStartView(View):
    def post(self,request):
        name = request.POST.get('name')
        identity = request.POST.get('identity')
        video_id = request.POST.get('video_id')

        path_format = '{}'.format(reverse('video_sub',kwargs={'video_id': video_id}))
        if not all([name,identity,video_id]):
            return redirect('{}?error={}'.format(path_format,'缺少必要字段'))


        result = check_and_get_video_type(IdentityType, identity, '非法的身份')
        if result.get('code') != 0:
            return redirect('{}?error={}'.format(path_format,result['msg']))
        video = Video.objects.get(pk=video_id)
        try:
            VideoStar.objects.create(
                video = video,
                name = name,
                identity = identity,
            )
        except:
            return redirect('{}?error={}'.format(path_format,'创建失败'))
        return redirect(reverse('video_sub', kwargs={'video_id': video_id}))

class StarDelete(View):

    def get(self,request,star_id,video_id):
        VideoStar.objects.filter(id=star_id).delete()
        return redirect(reverse('video_sub', kwargs={'video_id': video_id}))
