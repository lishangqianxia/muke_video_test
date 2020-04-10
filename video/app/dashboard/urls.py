# coding:utf8

from django.contrib import admin
from django.urls import path
from .views.base import Index

urlpatterns = [
    path('', Index.as_view()),
]
