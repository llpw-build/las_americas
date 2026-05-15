from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('menu/', views.menu, name='menu'),
    path('book/', views.book_table, name='book_table'),
    path('my-bookings/', views.my_bookings, name ='my_bookings'),
    path('contact/', views.contact, name='contact'),
    path('create-booking/', views.create_booking, name='create_booking'),
    path('edit-booking/<int:booking_id>/', views.edit_booking, name='edit_booking'),
    path('delete-booking/<int:booking_id>'/, views.delete_booking, name='delete_booking')
]

