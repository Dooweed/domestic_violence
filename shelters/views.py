import geopy.distance
from django.shortcuts import render

from shelters.models import Shelter


def shelters_list(request):
    user_location = (float(request.GET.get('latitude')), float(request.GET.get('longitude')))
    if None in user_location:
        raise ValueError('Latitude and/or longitude were not provided')

    shelters = Shelter.objects.all()
    for shelter in shelters:
        shelter.distance = round(geopy.distance.geodesic(shelter.location, user_location).km, ndigits=1)

    context = {
        'shelters': sorted(shelters, key=lambda x: x.distance),
    }
    return render(request, 'shelters_list.html', context)
