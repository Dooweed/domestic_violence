from django.contrib import admin

from sos_records.models import SosRecord


admin.site.site_header = 'Be Safe'


@admin.register(SosRecord)
class SosRecordAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'phone', 'shelter', 'status')
    list_editable = ('status',)

