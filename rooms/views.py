from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import RoomCategory, Room
# from booking.forms import AvailabilityForm


class RoomCategoryList(ListView):
    """List view for room categories."""
    model = RoomCategory
    template_name = 'rooms/roomcategory_list.html'
    context_object_name = 'categories'


class RoomDetailView(DetailView):
    model = Room
    template_name = 'rooms/room_detail.html'
    context_object_name = 'room'
