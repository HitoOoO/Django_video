#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author  : Ch1ps8oy
# @Time    : 2022/2/12 13:35
# @FileName: base_render.py
# @Software: PyCharm

#配置mako模板
from mako.lookup import TemplateLookup
from django.template import RequestContext
from django.conf import  settings
from django.template.context import Context
from django.http import HttpResponse
from django.template.context_processors import csrf
from django.middleware.csrf import get_token
def render_to_response(request,template,data=None):
    context_instance = RequestContext(request)
    path = settings.TEMPLATES[0]['DIRS'][0]
    lookup = TemplateLookup(
        directories=[path],
        output_encoding='utf-8',
        input_encoding='utf-8'
    )
    mako_template = lookup.get_template(template)

    if not data:
        data={}
    if context_instance:
        context_instance.update(data)
    else:
        context_instance=Context(data)
    result = {}

    for d in context_instance:
        result.update(d)


    #csrf_token = csrf(request)["csrf_token"]
    #data['csrf_token'] = '<input type="hidden" name="csrfmiddlewaretoken" value="{0}" />'.format(csrf_token, "")
    result['request'] = request
    request.META["CSRF_COOKIE"] = get_token(request)
    result['csrf_token'] = ('<div style="display:none">'
                            '<input type="hidden" '
                            'name="csrfmiddlewaretoken" '
                            'value="{0}"/>'
                            '</div>'.format(request.META["CSRF_COOKIE"]))
    return HttpResponse(mako_template.render(**result))