from django.contrib import admin

from logistic.models import Product, Stock, StockProduct


# Register your models here.

class StockPositionInline(admin.TabularInline):
    model = StockProduct
    extra = 3


@admin.register(Product)
class SensorAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'description']


@admin.register(Stock)
class SensorAdmin(admin.ModelAdmin):
    list_display = ['id', 'address']
    inlines = [StockPositionInline]


