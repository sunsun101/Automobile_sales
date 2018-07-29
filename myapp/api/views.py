# from rest_framework.generics import ListAPIView
from myapp.models import Userprofile,Vehicles,Userlikes
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .serializers import UserSerializer,VehiclesSerializer,UserProfileSerializer,UserlikeSerializer
from rest_framework import viewsets
from rest_framework.decorators import detail_route
from rest_framework.response import Response
from rest_framework import status


# class UserListAPIView(ListAPIView):
# 	queryset = User.objects.all
# 	serializer_class = UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


    
    def create(self,request,*arg,**kwarg):
        data = request.data 
 
        user = authenticate(username=data['user_name'], password=data['password'])
        if user is not None:
            # A backend authenticated the credentials
            return Response({'userid':user.id,'boolean':True},status=status.HTTP_202_ACCEPTED)

        else:
            # No backend authenticated the credentials
             return Response({'boolean':False},status=status.HTTP_401_UNAUTHORIZED)

class UserProfileViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Userprofile.objects.all()
    serializer_class = UserProfileSerializer

    def create(self,request,*arg,**kwarg):
        
        serializer = UserProfileSerializer(data=request.data)
       
        name = request.data['user_name']
        psw  = request.data['password']

        if serializer.is_valid():
            serializer.save()
            user = User.objects.create_user(username=name, password=psw)
            user.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class VehicleViewSet(viewsets.ModelViewSet):
   
    queryset            = Vehicles.objects.all()
    serializer_class    = VehiclesSerializer


class UserlikeViewSet(viewsets.ModelViewSet):

    queryset            = Userlikes.objects.all()
    serializer_class    = UserlikeSerializer

    