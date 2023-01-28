from django.contrib import admin
from django.urls import path, include

from bot.views import telegram_view

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', include('sos_records.urls')),
    path('', include('shelters.urls')),

    path('bot/<bot_token>/', telegram_view, name='telegram_view'),
]
