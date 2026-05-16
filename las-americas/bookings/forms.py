from datetime import date
from django import forms
from .models import Booking



class BookingForm(forms.ModelForm):

    class Meta:
        model = Booking

        fields = [
            "table",
            "booking_date",
            "booking_time",
            "number_of_guests",
            "customer_message",
        ]

        widgets = {
            "booking_date": forms.DateInput(attrs={"type": "date"}),
            "booking_time": forms.TimeInput(attrs={"type": "time"}),
        }

        def clean(self):
            cleaned_data = super().clean()

            table = cleaned_data.get("table")
            booking_date = cleaned_data.get("booking_date")
            booking_time = cleaned_data.get("booking_time")
            number_of_guests = cleaned_data.get("number_of_guests")

            if booking_date and booking_date < date.today():
                raise forms.ValidationError(
                    "Bookings cannot be made for a date in the past."
                )

            if table and number_of_guests:
                if number_of_guests > table.capacity:
                    raise forms.ValidationError(
                        "The number of guests exceeds the selected table capacity."
                    )

            if table and booking_date and booking_time:

                existing_booking = Booking.objects.filter(
                    table=table,
                    booking_date=booking_date,
                    booking_time=booking_time,
                )

            if self.instance.pk:
                existing_booking = existing_booking.exclude(
                    pk=self.instance.pk
                )

            if existing_booking.exists():
                raise forms.ValidationError(
                    "This table is already booked at that date and time."
                )

            return cleaned_data