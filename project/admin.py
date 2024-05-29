from django.contrib import admin
from project import models

# Register your models here.
@admin.register(models.ProductForSale)
class AdminProductForSale(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'value',
        'seller'
    )
    ordering = '-id',
    search_fields = ('name', 'id', 'seller')
    list_editable = ('value', 'seller')
    list_per_page = 10
    list_max_show_all = 150
    list_display_links = 'id', 'name',

@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = 'name',
    ordering = '-id',