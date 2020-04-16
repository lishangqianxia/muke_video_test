# coding:utf8

from django.contrib import admin
from django.urls import path
from .views.base import Index
from .views.video import ExVideo

urlpatterns = [
    path('', Index.as_view(), name='client_index'),
    path('video/ex', ExVideo.as_view(), name='client_ex_video')
]
