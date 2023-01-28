from django.contrib import admin

from bot.models import UsernameId


@admin.register(UsernameId)
class UsernameIdAdmin(admin.ModelAdmin):
    list_display = ('username', 'telegram_id')
