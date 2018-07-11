from django.contrib.auth.models import User
from myapp.models import Vehicles,Userprofile
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ( 'username','password', 'email')

class UserProfileSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Userprofile
        fields = ( 'first_name','middle_name', 'last_name','gender','email','birth_date','user_name','password')
       

class VehiclesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Vehicles
        fields = ('vehicle_type', 'brand' , 'model_no', 'engine_power', 'price', 'description', 'image', 'user_id')




