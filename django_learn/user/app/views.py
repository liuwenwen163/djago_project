# coding: utf-8
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, reverse
from django.contrib.auth import login, logout, authenticate
from django.views.generic import View


class Regist(View):
    TEMPLATE = 'regist.html'

    def get(self, request):

        if request.user.is_authenticated:
            return redirect(reverse('login'))

        error = request.GET.get('error', '')

        return render(request, self.TEMPLATE, {'error': error})

    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        check_password = request.POST.get('checkpassword')

        if password != check_password:
            return redirect('/regist?error=密码不相同')

        exists = User.objects.filter(username=username).exists()
        if exists:
            return redirect('/regist?error=该用户已存在')

        # 存储用户,create_user会帮助我们自动加密密码
        user = User.objects.create_user(
            username=username,
            password=password
        )
        user.save()

        return redirect(reverse('login'))


class Login(View):
    TEMPLATE = 'login.html'

    def get(self, request):
        error = request.GET.get('error', '')

        return render(request, self.TEMPLATE, {'error': error})

    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')

        exists = User.objects.filter(username=username).exists()
        if not exists:
            return redirect('/login?error=没有该用户')

        user = authenticate(username=username, password=password)

        if user:
            login(request, user)
        else:
            return redirect('/login?error=密码错误')

        return redirect('/login')


class LogoutUser(View):
    def get(self, request):
        logout(request)

        return redirect(reverse('logout'))
