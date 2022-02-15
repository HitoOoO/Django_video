#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author  : Ch1ps8oy
# @Time    : 2022/2/13 15:06
# @FileName: auth.py
# @Software: PyCharm
import hashlib
from django.db import models
def hash_password(password):
    if isinstance(password,str):
        password = password.encode('utf-8')
    return hashlib.md5(password).hexdigest().upper()



class ClientUser(models.Model):
    username = models.CharField(max_length=50,null=False,unique=True)
    password = models.CharField(max_length=255,null=False)
    avatar = models.CharField(max_length=50,default='')
    gender = models.CharField(max_length=10,default='')
    birthday = models.DateTimeField(null=True,blank=True,default=None)
    status = models.BooleanField(default=True,db_index=True)
    created_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return 'username:{}'.format(self.username)

    @classmethod
    def add(cls,username,password,avatar='',gender='',birthday=None):
        return cls.objects.create(
            username=username,
            password=hash_password(password),
            avatar=avatar,
            gender=gender,
            birthday=birthday,
            status=True
        )

    @classmethod
    def get_user(cls,username,password):
        try:
            user = cls.objects.get(
                username = username,
                password=hash_password(password)
            )
            return user
        except:
            return None


    def update_password(self,old_password,new_password):
        hash_old_password = hash_password(old_password)

        if hash_old_password != self.password:
            return False

        hash_new_password = hash(new_password)

        self.password = hash_new_password
        self.save()
        return True

    def update_status(self):
        self.status = not self.status
        self.save()
        return True