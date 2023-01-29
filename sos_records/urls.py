from django.urls import path

from sos_records.views import index_view, sos_request, sos_records_list

app_name = 'sos_records'

urlpatterns = [
    path('', index_view, name='index'),
    path('sos_request', sos_request, name='sos_request'),
    path('sos_records_list/', sos_records_list, name='sos_records_list'),
]
