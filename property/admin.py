from django.contrib import admin
from .models import PropertyTable,Contacted
# Register your models here.

class PropertyAdmin(admin.ModelAdmin):
    list_display = ('property_name', 'timestamp', 'updated')

admin.site.register(PropertyTable,PropertyAdmin,)
admin.site.register(Contacted)