from django.http import HttpResponse
from django.template import loader


def index(request):
    template = loader.get_template('runner/index.html')
    return HttpResponse(template.render())


def video(request):
    template = loader.get_template('runner/video.html')
    return HttpResponse(template.render())
