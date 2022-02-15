#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author  : Ch1ps8oy
# @Time    : 2022/2/13 18:42
# @FileName: common.py
# @Software: PyCharm

def check_and_get_video_type(type_obj,type_value,message):
    try:
        type_obj(type_value)
    except:
        return {'code':-1,'msg':message}
    return {'code':0,'msg':'success'}