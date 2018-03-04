from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.contrib.auth.models import User
from .models import Userprofile

def index(request):
    return render(request, 'registration/index.html', { })

def home(request):
	#text = """<h1>welcome to my app </h1>"""
	#return HttpResponse(text)
	return render(request,"Automobile_sales/home.html",{})

def user_logout(request):
    logout(request)
    return render(request, "registration/index.html", { })

def user_login(request):
    username = request.POST['name']
    password = request.POST['psw']
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            login(request,user)
            return render(request, 'Automobile_sales/home.html', {'user': user})
        else:
            return render(request, 'registration/index.html', {'error': True })
    else:
        return render(request, 'registration/index.html', {'error': True })
