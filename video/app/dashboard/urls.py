# coding:utf8

from django.contrib import admin
from django.urls import path
from .views.base import Index
from .views.auth import Login, Logout, AdminManger, UpdateAdminStatus
from .views.ceshi import Ceshi

urlpatterns = [
    path('', Index.as_view(), name='dashboard_index'),
    path('login', Login.as_view(), name='login'),
    path('logout', Logout.as_view(), name='logout'),
    path('ceshi', Ceshi.as_view()),
    path('admin/manger', AdminManger.as_view(), name='admin_manger'),
    path('admin/manger/update/status', UpdateAdminStatus.as_view(), name='admin_update_status')
]
