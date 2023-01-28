from django.urls import path

from sos_records.views import index_view

app_name = 'sos_records'

urlpatterns = [
    path('', index_view, name='index'),
]