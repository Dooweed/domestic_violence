from django.contrib import admin

from sos_records.models import SosRecord


@admin.register(SosRecord)
class SosRecordAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'shelter')
