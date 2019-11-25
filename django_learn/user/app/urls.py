# encoding: utf-8
from django.urls import path
from .views import Regist, Login, LogoutUser

urlpatterns = [
    path('regist', Regist.as_view(), name='regist'),
    path('login', Login.as_view(), name='login'),
    path('logout', LogoutUser.as_view(), name='logout')
]

