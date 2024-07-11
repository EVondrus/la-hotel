from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import RoomCategory, Room


class RoomCategoryList(ListView):
    """ 
    List view for displaying room categories.

    This view retrieves a list of RoomCategory objects and renders them
    in the specified template. The room categories are ordered by price.
    """
    model = RoomCategory
    template_name = 'rooms/roomcategory_list.html'
    context_object_name = 'categories'
    ordering = ['price']


class RoomCategoryDetail(DetailView):
    """
    Detail view for displaying a single room category.

    This view retrieves a RoomCategory object based on the primary key (pk)
    and renders it in the specified template.
    """
    model = RoomCategory
    template_name = 'rooms/roomcategory_detail.html'
    context_object_name = 'category'
