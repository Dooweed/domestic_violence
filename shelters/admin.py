from django.contrib import admin
from django.utils.safestring import mark_safe

from shelters.models import Shelter, ShelterContactInfo


class ShelterContactInfoInlineAdmin(admin.StackedInline):
    fields = (('name', 'email'), ('phone', 'telegram'))
    extra = 0
    model = ShelterContactInfo


@admin.register(Shelter)
class ShelterAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'contacts')
    fields = ('name', 'address', ('latitude', 'longitude'))

    inlines = [ShelterContactInfoInlineAdmin]

    @admin.display(description='Контакты')
    def contacts(self, obj: Shelter):
        contact = obj.sheltercontactinfo_set.first()
        if contact is None:
            return '-'

        return mark_safe(f'<b>{contact.name}</b>, {contact.phone}')
