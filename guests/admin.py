from django.contrib import admin
from .models import Profile

# Register your models here.
class ProfileAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'user',
        'first_name',
        'last_name',
        'phone_number',
        'address',
        'city',
        'country',
        'postal_code',
        'date_of_birth',
    )

    search_fields = ('user', 'first_name', 'last_name', 'phone_number')

admin.site.register(Profile, ProfileAdmin)