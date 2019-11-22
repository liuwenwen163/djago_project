# encoding: utf-8
"""所有form表单都在这个文件下面"""

from django import forms
from django.forms import fields


class Auth(forms.Form):
    username = fields.CharField(max_length=18, required=True)
    password = fields.CharField(widget=forms.PasswordInput)



