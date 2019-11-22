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
        # 这里括号中的username对应前端input标签中的name属性
        # username = request.POST.get('username')
        # password = request.POST.get('password')

        form = Auth(request.POST)

        if form.is_valid():
            # cleaned_data 代表经过验证之后，纯正的数据
            username = form.cleaned_data('username')
            password = form.cleaned_data('password')

        print('username', username)
        print('password', password)
        return redirect('/regist')


