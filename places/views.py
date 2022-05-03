from textwrap import indent
from django.http import HttpResponse, JsonResponse
from django.template import loader
from django.shortcuts import render

from places.models import Place, Image

# Create your views here.
def show_map(request):
    template = loader.get_template('index.html')

    places_GeoJson = {
        'type': 'FeatureCollection',
        'features': []
    }
    
    for place in Place.objects.all():
        place_feature = {
            'type': 'Feature',
            'geometry': {
                'type': 'Point',
                'coordinates': [place.lat, place.lng]
            },
            'properties': {
                'title': place.title,
                'placeId': f'place_{place.id}',
                'detailsUrl': f'/place/{place.id}'
            }
        }
        places_GeoJson['features'].append(place_feature)
    

    context = {'places': places_GeoJson}
    return render(request, 'index.html', context)


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