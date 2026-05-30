from django.contrib import admin

from .models import (
    Appetizers,
    Beverages,
    Breakfast,
    Brunch,
    Burgers,
    Cocktails,
    Desserts,
    GlutenFree,
    KidsMenu,
    Order,
    OrderItem,
    Pasta,
    Pizza,
    Salads,
    Sandwiches,
    Seafood,
    Sides,
    Soups,
    Specials,
    Steaks,
    Vegan,
    Vegetarian,
)


class DishAdmin(admin.ModelAdmin):
    list_display = ("name", "price")
    search_fields = ("name", "description")


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 0
    readonly_fields = ("dish_name", "category", "quantity", "unit_price", "line_total")


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ("id", "full_name", "phone", "payment_method", "order_status", "total", "created_at")
    list_filter = ("payment_method", "order_status", "created_at")
    search_fields = ("full_name", "phone", "email", "address")
    inlines = [OrderItemInline]


for model in [
    Appetizers,
    Salads,
    Soups,
    Pasta,
    Pizza,
    Seafood,
    Steaks,
    Burgers,
    Sandwiches,
    Vegetarian,
    Vegan,
    GlutenFree,
    Desserts,
    Beverages,
    Cocktails,
    Breakfast,
    Brunch,
    KidsMenu,
    Sides,
    Specials,
]:
    admin.site.register(model, DishAdmin)
