# coding:utf-8
from django.shortcuts import render, redirect
from django.views.generic import View

class Regist(View):
    TEMPLATE = 'regist.html'

    def get(self, request):
        return render(request, self.TEMPLATE)

    def post(self, request):
        # 这里括号中的username对应前端input标签中的name属性
        username = request.POST.get('username')
        password = request.POST.get('password')

        print('username', username)
        print('password', password)
        return redirect('/regist')


