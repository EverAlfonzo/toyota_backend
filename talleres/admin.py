from django.contrib import admin

# Register your models here.
from django.contrib import admin

# Register your models here.
from talleres.forms import TallerForm
from talleres.models import Taller


@admin.register(Taller)
class TallerAdmin(admin.ModelAdmin):
    list_display = ['title','address','phones','image_tag']
    search_fields = ['title']
    readonly_fields = ('image_tag',)
    autocomplete_fields = ['city']
    form = TallerForm
