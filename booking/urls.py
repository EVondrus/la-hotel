from django.urls import path
from .views import AddBooking

app_name = 'booking'

urlpatterns = [
    path('', AddBooking.as_view(), name='add_booking')
]