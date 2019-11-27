# encoding:utf-8
# from django.http import HttpResponse
import time

from django.contrib.auth import login, logout
from django.shortcuts import render, redirect, reverse
from django.views.generic import View
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required, permission_required

from .consts import MessageType
from .models import Message
from .forms import MessageForm, RegisterForm, LoginForm


class Register(View):
    TEMPLATE = 'register.html'

    def get(self, request):
        data = {}
        return render(request, self.TEMPLATE, data)

    def post(self, request):
        data = {}
        form = RegisterForm(request.POST)
        data['error'] = form.non_field_errors # 获取表单整体的错误信息

        if not form.is_valid():
            return render(request, self.TEMPLATE, data)

        return redirect(reverse('lessonfive'))


class LoginView(View):
    TEMPLATE = 'login.html'

    def get(self, request):
        if request.user.is_authenticated:
            return redirect(reverse('lessonfive'))

        data = {}
        # 设置一个next参数，作为hidden元素传入到html页面中
        next_return = request.GET.get('next', '')
        data['next'] = next_return

        return render(request, self.TEMPLATE, data)

    def post(self, request):
        data = {}
        form = LoginForm(request.POST)

        if not form.is_valid():
            data['error'] = form.non_field_errors
            # 获取表单整体的错误信息
            return render(request, self.TEMPLATE, data)

        user = form.cleaned_data.get('user')
        if user:
            login(request, user)

        # 获取到html页面中隐藏元素next_return，知道跳转到哪里
        next_return = request.POST.get('next_return')
        if next_return:
            # 参数存在就跳转到上一个页面，不存在就跳转到最后的默认页面
            return redirect(next_return)

        return redirect(reverse('lessonfive'))


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

    @method_decorator(permission_required('app.view_message'))
    def get(self, request):
        data = {}

        search = request.GET.get('search', '')
        if search:
            messages = Message.objects.filter(content__contains=search)
        else:
            messages = Message.objects.all()

        data['messages'] = messages

        return render(request, self.TEMPLATE, data)


class LessonFive(View):
    TEMPLATE = 'five.html'

    @method_decorator(login_required)
    def get(self, request):
        data = {}
        data['form'] = MessageForm()

        return render(request, self.TEMPLATE, data)

    def post(self, request):
        form = MessageForm(request.POST)

        # 不通过验证，返回进行渲染错误
        if not form.is_valid():
            return render(request, self.TEMPLATE, {'form': form})

        content = form.cleaned_data.get('content')
        message_type = form.cleaned_data.get('message_type')

        print(request.user.id)
        Message.objects.create(
            content=content,
            message_type=message_type.value,
            created_time=time.time(),
            user_id=request.user.id
        )

        return redirect(reverse('fourpagetwo'))


class LogoutUser(View):
    def get(self, request):
        logout(request)

        return redirect(reverse('login'))

