from payment.models import Item
from django.contrib import admin

@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ('name','price')