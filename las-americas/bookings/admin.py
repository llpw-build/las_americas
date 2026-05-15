from django.contrib import admin
from .models import RestaurantTable, Booking

# Register your models here.

@admin.register(RestaurantTable)
class RestaurantTableAdmin(admin.ModelAdmin):
    list_display = ("table_number", "capacity", "is_available")


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = (
        "user",
        "table",
        "booking_date",
        "booking_time",
        "number_of_guests",
    )

    list_filter = (
        "booking_date",
        "table",
    )

    search_fields = (
        "user__username",
    )