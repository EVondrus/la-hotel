from django.urls import path
from .views import RoomCategoryList, RoomDetailView

app_name = 'rooms'

urlpatterns = [
    path('', RoomCategoryList.as_view(), name='roomcategory'),
    path('room/<int:pk>/', RoomDetailView.as_view(), name='room_detail'),
]


