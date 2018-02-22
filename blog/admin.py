from django.contrib import admin
# Import the UserProfile model individually.
from .models import UserProfile

# Register your models here.
admin.site.register(UserProfile)