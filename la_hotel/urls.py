from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("accounts/", include("allauth.urls")),
    path('profiles/', include('guests.urls')),
    path('admin/', admin.site.urls),
    path('summernote/', include('django_summernote.urls')),
    path('', include('home.urls')),
    path('rooms/', include('rooms.urls'), name='rooms'),
    path('booking/', include('booking.urls'), name='booking'),
]
