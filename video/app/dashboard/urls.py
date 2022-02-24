#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author  : Ch1ps8oy
# @Time    : 2022/2/11 13:39
# @FileName: urls.py
# @Software: PyCharm
from django.urls import path
from .views.base import Index
from .views.auth import Login,AdminManger,Logout,UpdateAdminStatus,ClientManager
from .views.video import (ExternaVideo,VideoSubView,
                          VideoStartView,StarDelete,
                          SubDelete,VideoUpdate,
                            VideoUpdateStatus)
from .views.comments import Comments

urlpatterns = [
    path('',Index.as_view(),name = 'dashboard_index'),
    path('login',Login.as_view(),name='login'),
    path('logout',Logout.as_view(),name='logout'),
    path('admin/manger',AdminManger.as_view(),name='admin_manger'),
    path('admin/manger/update/status',UpdateAdminStatus.as_view(),name='admin_update_status'),
    path('video/externa',ExternaVideo.as_view(),name='externa_video'),
    path('video/videosub/<int:video_id>',VideoSubView.as_view(),name='video_sub'),
    path('video/star',VideoStartView.as_view(),name='video_start'),
    path('video/star/delete/<int:star_id>/<int:video_id>',StarDelete.as_view(),name = 'star_delete'),
    path('video/sub/delete/<int:videosub_id>/<int:video_id>',SubDelete.as_view(),name='sub_delete'),
    path('video/update/<int:video_id>',VideoUpdate.as_view(),name='video_update'),
    path('video/update/status/<int:video_id>',VideoUpdateStatus.as_view(),name='video_update_status'),
    path('comment/status/<int:comment_id>/<int:video_id>',Comments.as_view(),name='comment_update_status'),
    path('client/user',ClientManager.as_view(),name='dashboard_client_user'),

]