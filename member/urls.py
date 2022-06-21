from django.urls import path
from . import views

urlpatterns = [
    path('join/',views.join, name='member/join.html'),
    path('login/',views.login, name='member/login.html'),
    path('myinfo/',views.myinfo, name='member/myinfo.html')
]