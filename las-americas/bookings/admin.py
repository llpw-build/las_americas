from django.contrib import admin
from .models import RestaurantTable, Booking

# Register your models here.

admin.site.register(RestaurantTable)
admin.site.register(Booking)