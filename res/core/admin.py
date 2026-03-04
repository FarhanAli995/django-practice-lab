from django.contrib import admin
from .models import Menucatagory

# Register your models here.

@admin.register(Menucatagory)
class MenucatagoryAdmin(admin.ModelAdmin):
    list_display = ("ID", "dishname", "dishdescription", "price", "dishimage", "isavailable")
    list_filter = ("isavailable",)
    search_fields = ("dishname", "dishdescription")