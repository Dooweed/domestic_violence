import geopy.distance
from django.http import HttpResponse
from django.shortcuts import render

from bot.utils import send_message_to_telegram
from shelters.models import Shelter
from sos_records.models import SosRecord


MESSAGE_TEMPLATE = """<b>{name}</b> нажал(а) кнопку <b>SOS</b> 🆘
<b>Адрес:</b> <i>{address}</i>
<b>Номер телефона:</b> <i>{phone}</i>"""


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

    message = MESSAGE_TEMPLATE.format(name=data['name'], address=data['address'], phone=data['phone'])
    for contact in closest_shelter.sheltercontactinfo_set.all():
        if contact.telegram:
            send_message_to_telegram(contact.telegram.replace('@', ''), message, user_location)

    return HttpResponse({'success': closest_shelter}, status=200)


def sos_records_list(request):
    sos_records = SosRecord.objects.all()

    return render(request, 'dashboard/sos_records.html', {'records': sos_records})


def dashboard(request):
    return render(request, 'dashboard/dashboard.html')
