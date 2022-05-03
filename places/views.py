from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from places.models import Place

# Create your views here.
def show_map(request):

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
                'detailsUrl': reverse('place-by-id', kwargs={'place_id':place.id})
            }
        }
        places_GeoJson['features'].append(place_feature)
    

    context = {'places': places_GeoJson}
    return render(request, 'index.html', context)


def retrive_place_by_id(request, place_id):
    place = get_object_or_404(Place, id=place_id)
    
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