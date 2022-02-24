#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author  : Ch1ps8oy
# @Time    : 2022/2/21 17:54
# @FileName: comment.py
# @Software: PyCharm
from django.db import models
from .auth import ClientUser
from .video import Video


class Comment(models.Model):
    content = models.TextField()
    status = models.BooleanField(default=True, db_index=True)
    video = models.ForeignKey(
        Video,
        related_name='comment',
        on_delete=models.SET_NULL,
        blank=True, null=True
    )
    user = models.ForeignKey(
        ClientUser,
        related_name='comment',
        on_delete=models.SET_NULL,
        blank=True, null=True
    )

    def __str__(self):
        return self.content

    def data(self):
        return {
            'id': self.id,
            'content': self.content,
            'video_id': self.video.id,
            'user_id': self.user.id,
            'username': self.user.username
        }

