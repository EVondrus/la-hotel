from django.urls import path
from .views import Profiles

app_name = 'guests'

urlpatterns = [
    path('user/<int:pk>/', Profiles.as_view(), name='profile'),
]