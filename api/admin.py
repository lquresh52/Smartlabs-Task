
from django.contrib import admin
from .models import Order, Item
# Register your models here.


admin.site.register(Order)
# admin.site.register(Item)
class ItemAdmin(admin.ModelAdmin):
    readonly_fields = ('date', )

admin.site.register(Item, ItemAdmin)