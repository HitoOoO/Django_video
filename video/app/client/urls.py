#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author  : Ch1ps8oy
# @Time    : 2022/2/11 13:38
# @FileName: urls.py
# @Software: PyCharm

from django.urls import path
from .views.base import Index
from .views.video import ExVideo

urlpatterns = [
    path('',Index.as_view(),name='client_index'),
    path('video/ex',ExVideo.as_view(),name='client_ex_video')

]