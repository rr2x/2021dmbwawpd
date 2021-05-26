from django.contrib import admin
from .models import Profile

# need to register model extension to show on admin page
admin.site.register(Profile)
