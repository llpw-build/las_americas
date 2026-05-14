from django.db import models

# Create your models here.
from django.conf import settings
from django.db import models


class RestaurantTable(models.Model):
    table_number = models.PositiveIntegerField(unique=True)
    capacity = models.PositiveIntegerField()
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return f"Table {self.table_number} - seats {self.capacity}"


class Booking(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="bookings"
    )

    table = models.ForeignKey(
        RestaurantTable,
        on_delete=models.CASCADE,
        related_name="bookings"
    )

    booking_date = models.DateField()
    booking_time = models.TimeField()
    number_of_guests = models.PositiveIntegerField()
    customer_message = models.TextField(blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["booking_date", "booking_time"]
        unique_together = ["table", "booking_date", "booking_time"]

    def __str__(self):
        return f"{self.user.username} - Table {self.table.table_number} on {self.booking_date}"