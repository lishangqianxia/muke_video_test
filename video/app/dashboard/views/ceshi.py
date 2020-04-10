# coding;utf-8

from django.views.generic import View
from app.libs.base_render import render_to_response
from django.shortcuts import render, redirect, reverse


class Ceshi(View):
    TEMPLATE = 'ceshi.html'

    def get(self, request):

        return render(request, self.TEMPLATE)