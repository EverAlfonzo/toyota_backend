from django.contrib import admin

# Register your models here.
from django.contrib import admin

# Register your models here.
from talleres.forms import TallerForm
from talleres.models import Taller, ServiceType, Service


@admin.register(Taller)
class TallerAdmin(admin.ModelAdmin):
    list_display = ['name', 'phone', 'address', 'image_tag']
    search_fields = ['name', 'phone']
    readonly_fields = ('image_tag',)
    autocomplete_fields = ['city']


@admin.register(ServiceType)
class ServiceTypeAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']


