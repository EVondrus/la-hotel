from django.urls import path
from .views import RoomCategoryList, RoomCategoryDetail

app_name = 'rooms'

urlpatterns = [
    path('', RoomCategoryList.as_view(), name='roomcategory'),
    path('<int:pk>/', RoomCategoryDetail.as_view(),
         name='roomcategory_detail'),
]
