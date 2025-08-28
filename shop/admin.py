
from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Product

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('pk','name','description', 'price')
    search_fields = ('name', 'description','pk')
    list_per_page= 5
    readonly_fields = ('pk',)
    list_editable = ('price',)