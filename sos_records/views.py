import geopy.distance
from django.http import HttpResponse
from django.shortcuts import render

from shelters.models import Shelter
from sos_records.models import SosRecord


def index_view(request):
    context = {}

    return render(request, 'index.html', context)


def sos_request(request):
    fields = ('name', 'address', 'phone', 'latitude', 'longitude')
    data = {item: request.GET.get(item) for item in fields}
    user_location = data['latitude'], data['longitude']

    for key, val in data.items():
        if val is None:
            raise ValueError(f'{key} is not passed in get params')

    shelters = Shelter.objects.all()
    closest_shelter = shelters[0]
    closest_shelter.distance = geopy.distance.geodesic(closest_shelter.location, user_location).km

    for shelter in shelters[1:]:
        shelter.distance = geopy.distance.geodesic(shelter.location, user_location).km

        if shelter.distance < closest_shelter.distance:
            closest_shelter = shelter

    print(closest_shelter)
    sos_record = SosRecord.objects.create(**data, shelter=closest_shelter)

    # TODO: send message in telegram

    return HttpResponse({'success': closest_shelter}, status=200)
