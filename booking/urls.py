from django.urls import path
from .views import(
    AddBooking, 
    BookingList, 
    EditBooking, 
    DeleteBooking,
    BookingSuccess
)

app_name = 'booking'

urlpatterns = [
    path('', AddBooking.as_view(), name='add_booking'),
    path('success/', BookingSuccess.as_view(), name='booking_success'),
    path('list/', BookingList.as_view(), name='booking_list'),
    path('edit/<int:pk>', EditBooking.as_view(), name='edit_booking'),
    path('delete/<int:pk>/', DeleteBooking.as_view(), name='delete_booking'),
]