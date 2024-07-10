from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import RoomCategory, Room
# from booking.forms import AvailabilityForm


class RoomCategoryList(ListView):
    """List view for room categories."""
    model = RoomCategory
    template_name = 'rooms/roomcategory_list.html'
    context_object_name = 'categories'
    ordering = ['price']


class RoomCategoryDetail(DetailView):
    model = RoomCategory
    template_name = 'rooms/roomcategory_detail.html'
    context_object_name = 'category'
