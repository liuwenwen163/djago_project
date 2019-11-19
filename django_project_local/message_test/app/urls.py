# encoding: utf-8
from django.urls import path
from .views import LessonThree

urlpatterns = [
    path('three/<str:message_type>', LessonThree.as_view(), name='one')
]
