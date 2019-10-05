from django.contrib import admin

# Register your models here.
from articles.models import Article


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title','content','image_tag']
    search_fields = ['title']
    readonly_fields = ('image_tag',)
