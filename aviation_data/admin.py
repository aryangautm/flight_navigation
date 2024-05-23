from django.contrib import admin

from .models import Airport, Flight


class AirportAdmin(admin.ModelAdmin):
    pass


class FlightAdmin(admin.ModelAdmin):
    pass


admin.site.register(Airport, AirportAdmin)
admin.site.register(Flight, FlightAdmin)
