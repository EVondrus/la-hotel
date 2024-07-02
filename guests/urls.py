from django.urls import path
from .views import Profiles, EditProfile

app_name = 'guests'

urlpatterns = [
    path('user/<int:pk>/', Profiles.as_view(), name='profile'),
    path('edit/<int:pk>/', EditProfile.as_view(), name='edit_profile')
]