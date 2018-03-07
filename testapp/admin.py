from django.contrib import admin
from testapp.models import *

@admin.register(Amenity)
class AmenityAdmin(admin.ModelAdmin):
    list_display = (
        'eng_name',
        'chi_name',
        'icon',
    )

@admin.register(Newobj)
class NewobjAdmin(admin.ModelAdmin):
    list_display = (
        'field1',
    )
