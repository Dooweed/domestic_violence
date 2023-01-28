from django.urls import path

from shelters.views import shelters_list

app_name = 'shelters'

urlpatterns = [
    path('shelters/', shelters_list, name='shelters_list'),
]
