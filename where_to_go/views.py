from django.http import HttpResponse
from django.template import loader


def welcome(request):
    template = loader.get_template('welcome.html')
    context = {}
    return HttpResponse(template.render(context, request))