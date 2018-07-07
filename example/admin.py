from django.contrib import admin

from .models import OpenWilson, CloseWilson


@admin.register(OpenWilson)
class OpenWilsonAdmin(admin.ModelAdmin):
    pass


@admin.register(CloseWilson)
class CloseWilsonAdmin(admin.ModelAdmin):
    pass
