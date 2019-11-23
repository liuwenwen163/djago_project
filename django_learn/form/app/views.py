# coding:utf-8
from django.shortcuts import render, redirect
from django.views.generic import View
from .forms import Auth


class Regist(View):
    TEMPLATE = 'regist.html'

    def get(self, request):
        form = Auth()

        return render(request, self.TEMPLATE, {'form': form})

    def post(self, request):
        form = Auth(request.POST)

        if form.is_valid():
            # cleaned_data 代表经过验证之后，纯正的数据
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            print('username', username)
            print('password', password)
        else:
            # 验证不通过，此时的form携带了non_field_errors，渲染错误消息
            return render(request, self.TEMPLATE, {'form': form})

        return redirect('/regist')


