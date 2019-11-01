from django.contrib import admin

# Register your models here.
from .models import Cart


class CartAdmin(admin.ModelAdmin):
    model = Cart
    list_display = ('full_name', 'cart_number', 'password', 'balance',)


admin.site.register(Cart, CartAdmin)
