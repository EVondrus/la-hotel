from django.urls import path
from .views import Profiles, EditProfile, DeleteProfile



urlpatterns = [
    path('delete-profile/<int:pk>/', DeleteProfile.as_view(), name='delete_profile'),
    path('edit/<int:pk>/', EditProfile.as_view(), name='edit_profile'),
    path('profile/<int:pk>/', Profiles.as_view(), name='profile'),
]