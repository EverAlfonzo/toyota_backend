from django.contrib import admin

# Register your models here.
from django.contrib import admin

from location.models import Department, City


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']
    fields = ['name']


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ['name','department']
    search_fields = ['name']
    list_filter = ['department']
    autocomplete_fields = ['department']