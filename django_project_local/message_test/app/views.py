# encoding:utf-8
# from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import View
from .consts import MessageType


class LessonThree(View):
    TEMPLATE = 'three.html'

    def get(self, request, message_type):
        data = {}

        try:
            message_type_obj = MessageType[message_type]
        except Exception as e:
            data['error'] = '没有这个消息类型 {}'.format(e)
            return render(request, self.TEMPLATE, data)

        message = request.GET.get('message', '没有获取到内容')

        if not message:
            data['error'] = '消息不可为空'
            return render(request, self.TEMPLATE, data)

        data['message'] = message
        data['message_type'] = message_type_obj

        return render(request, self.TEMPLATE, data)

