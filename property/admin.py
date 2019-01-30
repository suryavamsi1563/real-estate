from django.contrib import admin
from .models import Property
# Register your models here.

class PropertyAdmin(admin.ModelAdmin):
    list_display = ('property_name', 'timestamp', 'updated')

admin.site.register(Property,PropertyAdmin)