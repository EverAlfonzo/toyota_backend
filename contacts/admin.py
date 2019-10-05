from django.contrib import admin

# Register your models here.
from contacts.models import Contact


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['email','message','created_at']
    search_fields = ['email']
    readonly_fields = list_display

    def has_add_permission(self, request):
        return False

    #def has_delete_permission(self, request, obj=None):
    #    return False