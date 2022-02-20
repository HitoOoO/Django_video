#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author  : Ch1ps8oy
# @Time    : 2022/2/13 18:42
# @FileName: common.py
# @Software: PyCharm

from django.conf import settings
import os
import time
import shutil
from app.libs.base_qiniu import video_qiniu
from app.models import VideoSub,Video
def check_and_get_video_type(type_obj,type_value,message):
    try:
        type_obj(type_value)
    except:
        return {'code':-1,'msg':message}
    return {'code':0,'msg':'success'}

def remove_path(paths):
    for path in paths:
        if os.path.exists(path):
            os.remove(path)




def handle_video(video_file,video_id,number):
    in_path = os.path.join(settings.BASE_DIR,r'app\dashboard\temp')
    out_path = os.path.join(settings.BASE_DIR,r'app\dashboard\temp_out')
    name = '{}_{}'.format(int(time.time()),video_file.name)
    path_name = '\\'.join([in_path,name])

    temp_path = video_file.temporary_file_path()
    shutil.copy(temp_path,path_name)
    out_name = '{}_{}'.format(int(time.time()),video_file.name)
    out_path = r'\\'.join([out_path,out_name])
    command = 'ffmpeg -i {} -c copy {}.mp4'.format(path_name,out_path)
    os.system(command)
    out_name = '.'.join([out_path,'mp4'])
    if not os.path.exists(out_name):
        remove_path([out_name, path_name])
        return False
    url = video_qiniu.put(video_file.name,'.'.join([out_path,'mp4']))

    if url:
        video = Video.objects.get(pk=video_id)
        try:
            VideoSub.objects.create(
                video=video,
                url=url,
                number=number,
            )
            return True
        except:
            return False
        finally:
            remove_path([out_name, path_name])
    remove_path([out_name,path_name])
    return False

