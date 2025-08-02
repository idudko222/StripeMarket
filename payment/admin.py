from payment.models import Item, Order
from django.contrib import admin

@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ('name','price')


@admin.register(Order)
class Order(admin.ModelAdmin):
    list_display = ('user', 'total_amount', 'is_paid', 'created_at', 'updated_at')