from re import template
from django.http import HttpResponse
from django.template import loader


def welcome(request):
    template = loader.get_template('welcome.html')
    context = {}
    return HttpResponse(template.render(context, request))


def show_map(request):
    template = loader.get_template('index.html')
    context = {}
    return HttpResponse(template.render(context, request))