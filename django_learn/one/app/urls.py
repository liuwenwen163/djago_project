# encoding: utf-8
# 这里的导入要用django2.0以后的形式
from django.urls import path
from .views import Index

urlpatterns = [
    # 第一个参数：url
    # 第二个参数：视图函数
    # 第三个参数：别名
    path('<str:name>/<int:age>', Index.as_view(), name='index')
]

