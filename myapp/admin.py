from django.contrib import admin
from .models import Userprofile,Vehicles


class UserprofileModel(admin.ModelAdmin):
	list_display = ["id","first_name", "middle_name", "last_name" , "gender", "email","Acc_type"]
	search_fields = ["first_name", "last_name"]
	class Meta:
		model = Userprofile

class VehiclesModel(admin.ModelAdmin):
	list_display = ["user_id","vehicle_type", "brand", "model_no" , "engine_power", "price","description","image"]
	search_fields = ["vehicle_type", "brand"]
	class Meta:
		model = Vehicles

admin.site.register(Userprofile, UserprofileModel)

admin.site.register(Vehicles, VehiclesModel)

# Register your models here.
