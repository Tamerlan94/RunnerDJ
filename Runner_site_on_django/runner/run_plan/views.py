from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.template import loader


def runplan(request):
    template = loader.get_template('runplan/runplan.html')
    return HttpResponse(template.render())
