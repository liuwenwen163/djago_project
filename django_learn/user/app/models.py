# coding:utf-8
from django.db import models


class Apage(models.Model):
    """对应数据库中的：app_page表"""
    title = models.CharField(max_length=10)

    def __str__(self):
        return '{}'.format(self.title)

    # 创建 meta
    class Meta:
        permissions = [
            ('look_a_page', 'can get this A page message'),
            ('look_c_page', 'can look C page.')
        ]


class Bpage(models.Model):
    title = models.CharField(max_length=10)

    def __str__(self):
        return '{}'.format(self.title)

    class Meta:
        permissions = [
            ('look_b_page', 'can get this B page message')
        ]

