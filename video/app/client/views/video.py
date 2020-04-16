# coding:utf-8

from django.views.generic import View
from app.libs.base_render import render_to_response
from app.models import Video
from app.model.video import FromType


class ExVideo(View):
    TEMPLATE = 'client/video/video.html'

    def get(self, request):
        videos = Video.objects.exclude(from_to=FromType.custom)
        data = {'videos': videos}
        return render_to_response(request, self.TEMPLATE, data=data)
