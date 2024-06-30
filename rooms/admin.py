from django.contrib import admin
from .models import Room, RoomCategory
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.
@admin.register(RoomCategory)
class RoomCategoryAdmin(SummernoteModelAdmin):
    list_display = ['category', 'price', 'capacity']
    search_fields = ['category']
    summernote_fields = ('description',)

@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = ['room_number', 'avaliable', 'category']
    search_fields = ['room_number']
    list_filter = ['room_number', 'category', 'avaliable']



