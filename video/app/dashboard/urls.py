# coding:utf8

from django.contrib import admin
from django.urls import path
from .views.base import Index
from .views.auth import Login
from .views.ceshi import Ceshi

urlpatterns = [
    path('', Index.as_view(), name='dashboard_index'),
    path('login', Login.as_view(), name='dashboard_login'),
    path('ceshi', Ceshi.as_view())

]
