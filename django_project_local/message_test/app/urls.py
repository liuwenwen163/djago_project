# encoding: utf-8
from django.urls import path
from .views import LessonThree, LessonFourPageOne, LessonFourPageTwo, LessonFive, Register, LoginView, LogoutUser

urlpatterns = [
    path('three/<str:message_type>', LessonThree.as_view(), name='one'),
    path('fourPageOne/<str:message_type>', LessonFourPageOne.as_view()),
    path('fourPageTwo', LessonFourPageTwo.as_view(), name='fourpagetwo'),
    path('five', LessonFive.as_view(), name='lessonfive'),
    path('register', Register.as_view(), name='register'),
    path('login', LoginView.as_view(), name='login'),
    path('logout', LogoutUser.as_view(), name='logout'),
]
