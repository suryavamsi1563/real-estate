from django.contrib import admin
from .models import PropertyTable,PropertyDetails,Contacted
# Register your models here.

class PropertyAdmin(admin.ModelAdmin):
    list_display = ('property_name', 'timestamp', 'updated')

class PropertyDetailsAdmin(admin.ModelAdmin):
    list_display = ('property_id','property_area','property_buid_year')


admin.site.register(PropertyTable,PropertyAdmin,)
admin.site.register(PropertyDetails,PropertyDetailsAdmin)
admin.site.register(Contacted)