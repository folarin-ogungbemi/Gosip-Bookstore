from django.contrib import admin
from .models import UserProfile


# Register your models here.
@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = [
        'user', 'user_phone_number',
        'user_address_line_1', 'user_address_line_2',
        'user_city', 'user_zip', 'user_state', 'user_country'
    ]
    search_fields = ('user', 'user_city', 'user_country')
    list_filter = ('user', 'user_city', 'user_country')
