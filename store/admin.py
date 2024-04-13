from django.contrib import admin
from django.utils.html import format_html
from .models import *


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'description']


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'admin_description', 'admin_price', 'admin_image', 'category']

    list_filter = ['category', 'name', 'price']

    def max_length(self, text, long=20):
        if len(text) > long:
            return f"{text[:long]}..."
        return text

    def admin_description(self, obj):
        return self.max_length(text=obj.description)

    def admin_price(self, obj):
        # return f"${obj.price}"
        return format_html(
            f'<p style="background: green; padding: 3px; border-radius: 10px; text-align:center; color: white;"> ${obj.price:,.2f}</p>')

    def admin_image(self, obj):
        if obj.image_url:
            return format_html('<a href="{}" target="_blank"><img src="{}" height="30"/></a>', obj.image_url,
                               obj.image_url)
        return format_html('<img src="#" alt="no" />')


admin.site.register(Customer)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(ShippingAddress)
