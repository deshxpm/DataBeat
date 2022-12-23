from django.contrib import admin
from .models import *
# Register your models here.


class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('email', 'username', 'name',
    				'password')
    list_filter = ('email', 'username')
    search_fields = ('email', 'username')




admin.site.register(UserProfile, UserProfileAdmin)    
