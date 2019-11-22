# encoding:utf-8
# from django.http import HttpResponse
import time

from django.shortcuts import render, redirect, reverse
from django.views.generic import View
from .consts import MessageType

from .models import Message


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


class LessonFourPageOne(View):
    TEMPLATE = 'four_page_one.html'

    def get(self, request, message_type):
        data = {}

        # 如果传入的消息没有这个类型，处理异常
        try:
            message_type_obj = MessageType[message_type]
        except Exception as e:
            data['error'] = '没有这个消息类型 {}'.format(e)
            return render(request, self.TEMPLATE, data)

        message = request.GET.get('message', '')
        if not message:
            data['error'] = '消息不可为空'
            return render(request, self.TEMPLATE, data)

        # message的内容和都正常的话，将有关信息写入数据库
        Message.objects.create(
            content=message,
            message_type=message_type_obj.value,
            created_time=time.time()
        )

        return redirect(reverse('fourpagetwo'))


class LessonFourPageTwo(View):
    TEMPLATE = 'four_page_two.html'

    def get(self, request):
        data = {}

        search = request.GET.get('search', '')
        if search:
            messages = Message.objects.filter(content__contains=search)
        else:
            messages = Message.objects.all()

        data['messages'] = messages

        return render(request, self.TEMPLATE, data)
