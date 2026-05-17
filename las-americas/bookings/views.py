from django.shortcuts import render, redirect, get_object_or_404
from .models import Booking
from .forms import BookingForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

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

@login_required
def create_booking(request):

    if request.method == "POST":
        form = BookingForm(request.POST)

        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = request.user
            booking.save()

            messages.success(
                request,
                "Bookings created successfully.",
            )

            return redirect("my_bookings")

    else:
        form = BookingForm()

    return render(
        request,
        "create_booking.html",
        {"form": form},
    )

@login_required
def my_bookings(request):

    bookings = Booking.objects.filter(user=request.user)

    context = {"bookings": bookings}

    return render(
        request,
        'my_bookings.html',
        context,
    )

@login_required
def edit_booking(request, booking_id):

    booking = get_object_or_404(
        Booking,
        id=booking_id,
        user=request.user
    )

    if request.method == "POST":

        form = BookingForm(
            request.POST,
            instance=booking
        )

        if form.is_valid():
            form.save()

            messages.success(
                request,
                "Bookings created successfully.",
            )

            return redirect("my_bookings")

    else:

        form = BookingForm(instance=booking)

    return render(
        request,
        "edit_booking.html",
        {
            "form": form,
            "booking": booking,
        },
    )

@login_required
def delete_booking(request, booking_id):

    booking = get_object_or_404(
        Booking,
        id=booking_id,
        user=request.user
    )

    if request.method == "POST":

        booking.delete()
        
        messages.success(
            request,
            "Booking deleted successfully"
        )

        return redirect("my_bookings")

    return render(
        request,
        "delete_booking.html",
        {
            "booking": booking
        },
    )