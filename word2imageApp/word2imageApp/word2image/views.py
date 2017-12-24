from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse


def index(request):
    context = {}
    return render(request, 'index.html', context)


def prepare_data(request):
    template = loader.get_template('prepareData.html')
    context = {}
    return HttpResponse(template.render(context, request))


def research_images(request):
    template = loader.get_template('researchData.html')
    context = {}
    return HttpResponse(template.render(context, request))
