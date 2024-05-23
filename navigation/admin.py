from django.contrib import admin

from .models import Airport, Route


class AirportAdmin(admin.ModelAdmin):
    pass


class RouteAdmin(admin.ModelAdmin):
    pass


admin.site.register(Airport, AirportAdmin)
admin.site.register(Route, RouteAdmin)
