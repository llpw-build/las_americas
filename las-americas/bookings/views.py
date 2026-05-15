from django.shortcuts import render, redirect, get_object_or_404
from .models import Booking
from .forms import BookingForm

# Create your views here.
def home(request):
    return render(request, 'index.html')

def menu(request):
    return render(request, 'menu.html')

def book_table(request):
    return render(request, 'book_table.html')

def my_bookings(request):
    return render(request, 'my_bookings.html')

def contact(request):
    return render(request, 'contact.html')

def create_booking(request):

    if request.method == "POST":
        form = BookingForm(request.POST)

        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = request.user
            booking.save()

            return redirect("my_bookings")

    else:
        form = BookingForm()

    return render(
        request,
        "create_booking.html",
        {"form": form},
    )