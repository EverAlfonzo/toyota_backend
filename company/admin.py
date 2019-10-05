from django.contrib import admin

# Register your models here.
from django.http.response import HttpResponseRedirect

from company.models import Company, CompanyImage, Brand, Model


class CompanyImageInline(admin.TabularInline):
    model = CompanyImage
    readonly_fields = ('image_tag',)

@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ['name','description','phone','address','image_tag']
    search_fields = ['name']
    readonly_fields = ('image_tag',)
    inlines = [CompanyImageInline]


    def changelist_view(self, request, extra_context=None):
        obj = Company.objects.first()
        if obj:
            return HttpResponseRedirect('/admin/company/company/%s/change' % obj.pk)
        return self.add_view(request,form_url='',extra_context=extra_context)


    
    def add_view(self, request, form_url='', extra_context=None):
        obj = Company.objects.first()
        if obj:
            return HttpResponseRedirect('/admin/company/company/%s/change'%obj.pk)
        return super(CompanyAdmin, self).add_view(request,form_url=form_url,extra_context=extra_context)


class ModelInline(admin.TabularInline):
    model = Model


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ['name','image_tag']
    search_fields = ['name']
    readonly_fields = ('image_tag',)
    inlines = [ModelInline]