from django.contrib import admin
from .models import Orders

# Register your models here.
@admin.register(Orders)
class OrdersAdmin(admin.ModelAdmin):

    list_display = ('name', 'phone', 'address', 'created_date', 'status')

    fields = ('name', 'phone', 'address', 'product', 'created_date', 'status')
    readonly_fields = ('name', 'phone', 'address', 'product', 'created_date')

    class Meta:
        model = Orders