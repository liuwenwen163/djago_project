# coding: utf-8
from django.contrib.auth.models import User, Permission
from django.db.models import Q
from django.http import Http404
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

        return redirect(reverse('login'))


class A(View):
    TEMPLATE = 'a.html'
    TEMPLATE_ERROR = 'error.html'

    def get(self, request):
        if not request.user.is_authenticated:
            return redirect('/login')

        print(request.user.user_permissions)

        if not request.user.has_perm('app.look_a_page'):
            print('test')
            return render(request, self.TEMPLATE_ERROR, {'error': '您无权访问该页'})

        return render(request, self.TEMPLATE)


class B(View):
    TEMPLATE = 'b.html'
    TEMPLATE_ERROR = 'error.html'

    # def get(self, request):
    #     """
    #     两种写法:
    #     第一种写法:
    #     下面的 filter 查询验证了组有没有对应的权限
    #     """
    #     if not request.user.is_authenticated:
    #         return redirect('/login')
    #
    #     b_permission = Permission.objects.filter(
    #         codename='look_b_page').first()
    #     # 在用户的用户权限 或 组权限中看看能否找到对应的权限
    #     users = User.objects.filter(
    #         Q(groups__permissions=b_permission) |
    #         Q(user_permissions=b_permission)
    #     ).distinct()
    #
    #     print(users)
    #     if request.user not in users:
    #         raise Http404
    #
    #     return render(request, self.TEMPLATE)


    from django.utils.decorators import method_decorator
    from django.contrib.auth.decorators import login_required, permission_required

    @method_decorator(login_required)
    @method_decorator(permission_required('app.look_b_page'))
    def get(self, request):
        """
        第二种写法:
        装饰器实现了验证用户有没有登录, 账号是否is_active.
        用户有无权限,
        permission这个装饰器会去组和user两个表里都去查找权限
        优点:方便
        缺点:验证不通过只能跳转到一个固定的页面
        """
        return render(request, self.TEMPLATE)
