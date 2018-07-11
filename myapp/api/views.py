# from rest_framework.generics import ListAPIView
from myapp.models import Userprofile,Vehicles
from django.contrib.auth.models import User
from .serializers import UserSerializer,VehiclesSerializer,UserProfileSerializer
from rest_framework import viewsets



# class UserListAPIView(ListAPIView):
# 	queryset = User.objects.all
# 	serializer_class = UserSerializer

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer

class UserProfileViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Userprofile.objects.all()
    serializer_class = UserProfileSerializer


class VehicleViewSet(viewsets.ModelViewSet):
   
    queryset = Vehicles.objects.all()
    serializer_class = VehiclesSerializer