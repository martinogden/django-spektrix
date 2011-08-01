from django.contrib import admin
from django.db import models
from django.contrib.contenttypes import generic
from django.db.models import get_model
from django.forms.widgets import TextInput

from spektrix import settings
from spektrix.models import Attribute


event_model = get_model(*settings.SPEKTRIX_EVENT_MODEL.split('.'))
time_model = get_model(*settings.SPEKTRIX_TIME_MODEL.split('.'))


class TimeInlineAdmin(admin.TabularInline):
    verbose_name_plural = 'Event Times'
    verbose_name = 'Event Time'
    model = time_model
    fields = ['Time', 'Capacity', 'SeatsSold', 'SeatsLocked', 'SeatsSelected', 'SeatsAvailable', 'SeatsReserved', 'OnSaleOnWeb']
    readonly_fields = fields
    extra = 0
    can_delete = False


class AttributeInlineAdmin(generic.GenericTabularInline):
    model = Attribute
    extra = 0
    can_delete = False
    formfield_overrides = {
        models.TextField: {'widget': TextInput},
    }

    fields = ['Name', 'Value', 'tag']
    readonly_fields = fields


class EventAdmin(admin.ModelAdmin):
    list_display = ['Name', 'FirstInstance', 'LastInstance', 'is_moderated']
    list_editable = ['is_moderated']

    inlines = [TimeInlineAdmin, AttributeInlineAdmin]

    readonly_fields = ['Name', 'Description', 'Html', 'OnSaleOnWeb',
        'FirstInstance', 'LastInstance', 'Duration',
        'ImageUrl', 'ThumbnailUrl',]

    fieldsets = (
        (None, {
            'fields': ('is_moderated', 'Name', 'Description', 'Html', 'OnSaleOnWeb')
        }),
        ('Dates / Times', {
            'fields': ('FirstInstance', 'LastInstance', 'Duration')
        }),
        ('Images', {
            'classes': ('collapse',),
            'fields': ('ImageUrl', 'ThumbnailUrl')
        }),
    )

# try:
#     admin.site.register(event_model, EventAdmin)
# except admin.sites.AlreadyRegistered:
#     pass
