#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author  : Ch1ps8oy
# @Time    : 2022/2/11 13:38
# @FileName: urls.py
# @Software: PyCharm

from django.urls import path
from .views.base import Index
from .views.video import ExVideo,VideoSub,CusVideo
from .views.auth import User,Regist,Logout

urlpatterns = [
    path('',Index.as_view(),name='client_index'),
    path('video/ex',ExVideo.as_view(),name='client_ex_video'),
    path('video/custom',CusVideo.as_view(),name='client_cus_video'),
    path('video/<int:video_id>',VideoSub.as_view(),name='client_video_sub'),
    path('auth',User.as_view(),name='client_auth'),
    path('auth/regist',Regist.as_view(),name='client_regist'),
    path('auth/logout',Logout.as_view(),name='client_logout')

]