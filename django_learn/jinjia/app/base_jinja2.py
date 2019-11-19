# encoding: utf-8
from jinja2 import Environment
from django.contrib.staticfiles.storage import staticfiles_storage
from django.urls import reverse


def environment(**options):
    # 添加基础的配置文件
    env = Environment(**options)

    # 配置一些全局的数据
    env.globals.update({
        'static': staticfiles_storage.url,
        'url': reverse
    })
    return env

