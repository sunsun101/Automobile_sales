from django.contrib import admin
from .models import Userprofile,Vehicles

# from django.contrib.auth.admin import UserAdmin
# from .models import User

admin.site.register(Userprofile)
admin.site.register(Vehicles)

# Register your models here.
