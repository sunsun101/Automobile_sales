from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from .models import Userprofile
from .models import Vehicles




def index(request):
	return render(request, 'registration/index.html', { })

def home(request):
    if not request.session.get('logged_in'):
        return HttpResponseRedirect('/')
    instance = request.user
    userid   = instance.id
    queryset = Vehicles.objects.filter(user_id = userid)
    return render(request,"Automobile_sales/home.html",{'queryset': queryset })

def user_logout(request):
    logout(request)
    try:
        del request.session['logged_in']
    except KeyError:
       return HttpResponseRedirect('/')
    
    return render(request, "registration/index.html", { })

def Register(request):
	return render(request,"registration/register.html", {})

def user_login(request):
   
    username = request.POST['name']
    password = request.POST['psw']

    queryset_user = Userprofile.objects.filter(user_name = username)
    if(queryset_user[0].Acc_type == 'company'):
    
        user = authenticate(username=username, password=password)
        if user is not None:
            # if user.is_active:
                login(request,user)
                request.session['logged_in'] = True
                instance = request.user
                userid   = instance.id
                queryset = Vehicles.objects.filter(user_id = userid)
                return HttpResponseRedirect('/home/')
                
            # else:
            #     return render(request, 'registration/index.html', {'error': True })
        else:
            return render(request, 'registration/index.html', {'error': True })
    return render(request, 'registration/index.html', {'msg': True })

def signup(request):
    if request.POST:
        first_name  = request.POST.get('first-name')
        middle_name = request.POST.get('middle-name')
        last_name   = request.POST.get('last-name')
        name        = request.POST.get('user-name')
        emailInput  = request.POST.get('email')
        psw         = request.POST.get('password')
        gen         = request.POST.get('gender')
        bday        = request.POST.get('bday')
       
    # user = authenticate(username=name, password=psw)
    # if user is not None:
    #     if user.is_active:
    #         user_created = True
    #     else:
    #         user_created = False
            
    # else:    
        p = Userprofile(first_name=first_name,middle_name =middle_name,last_name=last_name, user_name=name,birth_date=bday, email= emailInput, password=psw, gender=gen)
        p.save()        
        user = User.objects.create_user(username=name, password=psw)
        user.save()
       
    return render(request, 'registration/index.html', {})

          


def vehicle_upload(request):
    if not request.session.get('logged_in'):
        return HttpResponseRedirect('/')
    return render(request,'Automobile_sales/Vehicle_upload.html', {})


def vehicle_store(request):
    if not request.session.get('logged_in'):
        return HttpResponseRedirect('/')
    if request.POST:
        Vehicle_type  = request.POST.get('Vehicle_type')
        Brand         = request.POST.get('brand')
        Model_no      = request.POST.get('model')
        Price         = request.POST.get('price')
        Description   = request.POST.get('description')
        Image         = request.FILES.get('imagefile')

    instance = request.user
    userid   = instance.id

   
    vehicle = Vehicles(vehicle_type = Vehicle_type, brand = Brand, model_no = Model_no, price = Price, description = Description, image = Image, user_id = userid )
    vehicle.save()
    
    queryset = Vehicles.objects.filter(user_id = userid)
    return HttpResponseRedirect('/home/')



