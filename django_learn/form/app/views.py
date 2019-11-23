# coding:utf-8
from django.shortcuts import render, redirect
from django.views.generic import View
from .forms import AuthModelForm
from .models import Auth as AuthModel


class Regist(View):
    TEMPLATE = 'regist.html'

    def get(self, request):
        # 从数据获取数据
        user = AuthModel.objects.filter(pk=3).first()
        if user:
            form = AuthModelForm(instance=user)
        else:
            form = AuthModelForm()

        return render(request, self.TEMPLATE, {'form': form})

    def post(self, request):
        form = AuthModelForm(request.POST)

        if form.is_valid():
            # cleaned_data 代表经过验证之后，纯正的数据
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            # 如果表单验证成功了，就将数据存储到数据库
            form.save()
        else:
            # 验证不通过，此时的form携带了non_field_errors，渲染错误消息
            return render(request, self.TEMPLATE, {'form': form})

        return redirect('/regist')


