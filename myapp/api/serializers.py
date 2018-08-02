from django.contrib.auth.models import User
from myapp.models import Vehicles,Userprofile,Userlikes
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ( 'id','username','password', 'email')

class UserProfileSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Userprofile
        fields = ( 'first_name','middle_name', 'last_name','gender','email','birth_date','user_name','password')
       

class VehiclesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Vehicles
        fields = ('id','vehicle_type', 'brand' , 'model_no', 'engine_power', 'price', 'description', 'image', 'user_id')

class UserlikeSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Userlikes
		fields = ('company_id','liker_id','vehicle_id','month')
			
	
