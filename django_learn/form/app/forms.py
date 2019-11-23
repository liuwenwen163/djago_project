# encoding: utf-8
"""所有form表单都在这个文件下面"""

from django import forms
from django.forms import fields


class Auth(forms.Form):
    username = fields.CharField(
        # max_length=11,
        required=False,
        label="username",
        widget=forms.TextInput(
            attrs={'placeholder': '最大不可超过10个字符'}),
    )
    password = fields.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': '请输入密码'}),
        label="password",
        required=False,
        min_length=10,
        error_messages={'min_length': '最小不能低于10个字符'}
    )

    # def clean(self):
    #     """
    #     clean是统一验证
    #     进行验证时，会自动调用 clean
    #     """
    #     # 如果没有获取到对应的字段，就赋予一个空值
    #     username = self.cleaned_data.get('username', '')
    #     password = self.cleaned_data.get('password', '')
    #
    #     if not username:
    #         raise forms.ValidationError('用户名不可以为空')
    #
    #     if len(username) > 10:
    #         raise forms.ValidationError('用户名最大不能超过10')
    #
    #     if not password:
    #         raise forms.ValidationError('密码不可以为空')

    def clean_username(self):
        username = self.cleaned_data.get('username', '')

        if not username:
            raise forms.ValidationError('用户名不可以为空')

        if len(username) > 10:
            raise forms.ValidationError('用户名最大不能超过10')

    def clean(self):
        """单独验证和集体验证结合"""
        password = self.cleaned_data.get('password', '')

        if not password:
            raise forms.ValidationError('密码不可以为空')


    # def clean_password(self):
    #     password = self.cleaned_data.get('password', '')
    #
    #     if not password:
    #         raise forms.ValidationError('密码不可以为空')
    #
    #     if len(password) > 8:
    #         raise forms.ValidationError('密码不能超过8位')

