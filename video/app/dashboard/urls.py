# coding:utf8

from django.contrib import admin
from django.urls import path
from .views.base import Index
from .views.auth import Login, AdminManger

urlpatterns = [
    path('', Index.as_view(), name='dashboard_index'),
    path('login', Login.as_view(), name='dashboard_login'),
    path('admin/manger', AdminManger.as_view(), name='admin_manger')
]
