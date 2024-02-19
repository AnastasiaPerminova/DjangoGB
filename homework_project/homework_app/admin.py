from django.contrib import admin
from .models import Customer, Product, Order


class CustomerAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'phone', 'address', 'registration_date']
    search_fields = ['name']
    ordering = ['-registration_date']
    list_filter = ['address', 'registration_date']

    # actions = [reset_birthday]
    fieldsets = [
        (
            None,
            {
                'classes': ['wide'],
                'fields': ['name', 'email'],
            },
        ),
        (
            'Подробности',
            {
                'classes': ['collapse'],
                'description': 'Дополнительные контакты',
                'fields': ['phone', 'address'],
            },
        ),

    ]


@admin.action(description="Обнулить количество товара")
def reset_quantity(modeladmin, request, queryset):
    queryset.update(quantity=0)


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'quantity', 'addition_date']
    search_fields = ['name']
    ordering = ['price']
    list_filter = ['price', 'quantity']
    actions = [reset_quantity]
    fieldsets = [
        (
            None,
            {
                'classes': ['wide'],
                'fields': ['name', 'price', 'quantity'],
            },
        ),
        (
            'Описание',
            {
                'classes': ['collapse'],
                'description': 'Описание товара',
                'fields': ['description', 'image'],
            },
        ),

    ]


class OrderProductInline(admin.TabularInline):
    model = Order.product.through


class OrderAdmin(admin.ModelAdmin):
    list_display = ['pk', 'customer', 'order_date', 'total_price']
    search_fields = ['customer']
    ordering = ['pk']
    list_filter = ['customer', 'order_date']
    model = Product
    inlines = [OrderProductInline, ]
    fieldsets = [
        (
            None,
            {
                'classes': ['wide'],
                'fields': ['customer', 'total_price'],
            },
        ),

    ]


# Register your models here.
admin.site.register(Customer, CustomerAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Order, OrderAdmin)
