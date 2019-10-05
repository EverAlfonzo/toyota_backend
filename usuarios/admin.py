from django.contrib import admin

# Register your models here.
from usuarios.models import Profile


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'phone', 'image_tag']
    search_fields = ['user__username', 'phone']
    readonly_fields = ('image_tag',)
    autocomplete_fields = ['user']
