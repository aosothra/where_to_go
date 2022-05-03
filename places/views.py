from textwrap import indent
from django.http import HttpResponse, JsonResponse
from django.template import loader
from django.shortcuts import render

from places.models import Place, Image

# Create your views here.
def show_map(request):
    template = loader.get_template('index.html')
    context = {}
    return HttpResponse(template.render(context, request))


def retrive_place_by_id(request, place_id):
    try:
        place = Place.objects.prefetch_related('images').get(id=place_id)
    except Place.DoesNotExist:
        return JsonResponse({'error':'place not found'})

    place_serialized = {
        "title": place.title,
        "imgs": [image.image_file.url for image in place.images.all()],
        "description_short": place.description_short,
        "description_long": place.description_long,
        "coordinates": {
            "lat": place.lat,
            "lng": place.lng
        }
    }

    return JsonResponse(
            place_serialized, 
            safe=False, 
            json_dumps_params={'ensure_ascii': False, 'indent':2}
        )