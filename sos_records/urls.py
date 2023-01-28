from django.urls import path

from sos_records.views import index_view, sos_request

app_name = 'sos_records'

urlpatterns = [
    path('', index_view, name='index'),
    path('sos_request', sos_request, name='sos_request'),
]
