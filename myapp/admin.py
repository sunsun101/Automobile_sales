from django.contrib import admin
from .models import Userprofile,Vehicles,Userlikes
from django.contrib.auth.models import User

class UserprofileModel(admin.ModelAdmin):
	list_display = ["id","first_name", "middle_name", "last_name" ,"company_name", "gender", "email","Acc_type","birth_date"]
	search_fields = ["first_name", "last_name"]
	class Meta:
		model = Userprofile

class VehiclesModel(admin.ModelAdmin):
	list_display = ["id","user_id","vehicle_type", "brand", "model_no" , "engine_power", "price","description","image","like_count"]
	search_fields = ["vehicle_type", "brand"]
	class Meta:
		model = Vehicles

class UserlikeModel(admin.ModelAdmin):
	list_display = ["company_id","vehicle_id","liker_id","date","rating"]
	search_fields = ["company_id", "vehicle_id","date"]
	class Meta:
		model = Userlikes

admin.site.register(Userprofile, UserprofileModel)

admin.site.register(Vehicles, VehiclesModel)

admin.site.register(Userlikes, UserlikeModel)
# Register your models here.
