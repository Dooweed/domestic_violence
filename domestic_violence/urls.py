from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', include('sos_records.urls')),
    path('', include('shelters.urls')),
]
