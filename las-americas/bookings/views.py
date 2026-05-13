from django.shortcuts import render

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