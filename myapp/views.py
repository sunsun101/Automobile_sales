from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from .models import Userprofile
from .models import Vehicles,Userlikes
from django.http import JsonResponse




def index(request):
	return render(request, 'registration/index.html', { })

def home(request):
    if not request.session.get('logged_in'):
        return HttpResponseRedirect('/')
    instance = request.user
    userid   = instance.id
    queryset = Vehicles.objects.filter(user_id = userid)

    return render(request,"Automobile_sales/home.html",{'queryset': queryset, 'home_or_userhomepage': True, 'company':True,'userid':userid})


def userhome(request):
    if not request.session.get('logged_in'):
        return HttpResponseRedirect('/')
    instance = request.user
    userid   = instance.id
    queryset = Vehicles.objects.raw('''SELECT * from myapp_vehicles LEFT JOIN myapp_userlikes on myapp_vehicles.id = myapp_userlikes.vehicle_id and myapp_userlikes.liker_id = %s''', [userid])

    return render(request,"Automobile_sales/userhome.html",{'queryset': queryset,'home_or_userhomepage': True,'userid':userid})

def adminpage(request):
    if not request.session.get('logged_in'):
        return HttpResponseRedirect('/')
    return render(request,'Automobile_sales/adminpage.html',{'admin':True})




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

    if queryset_user:

        if(queryset_user[0].Acc_type == 'C'):
        
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

        elif(queryset_user[0].Acc_type == 'I'):
            user = authenticate(username=username, password=password)
            if user is not None:
                # if user.is_active:
                    login(request,user)
                    request.session['logged_in'] = True
                    instance = request.user
                    userid   = instance.id
                   

                    return HttpResponseRedirect('/userhome/')
                    
               
            else:
                return render(request, 'registration/index.html', {'error': True })

        elif(queryset_user[0].Acc_type == 'A'):
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_superuser:
                    login(request,user)
                    request.session['logged_in'] = True
                    
                    return HttpResponseRedirect('/adminpage/')


        else:

            return render(request, 'registration/index.html', {'msg': True })

    else:
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
        p = Userprofile(first_name=first_name,middle_name =middle_name,last_name=last_name,company_name = '', user_name=name,birth_date=bday, email= emailInput, password=psw, gender=gen)
        p.save()        
        user = User.objects.create_user(username=name, password=psw)
        user.save()


       
    return render(request, 'registration/index.html', {})

          
def create_account(request):
    if request.POST:
        company_name    = request.POST.get('company_name')
        username        = request.POST.get('username')
        psw             = request.POST.get('password')
       
    p = Userprofile(first_name='',middle_name ='',last_name='',company_name = company_name, user_name=username, email= '', password=psw, gender='',Acc_type='C')
    p.save()        
    user = User.objects.create_user(username=username, password=psw)
    user.save()

    return HttpResponseRedirect('/adminpage/')


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



def likecounterIncrement(request):

    instance    = request.user
    user_id     = instance.id
    
    vehicle_id  = request.GET.get('id', None)
    queryset    = Vehicles.objects.filter(id = vehicle_id)
    company_id  = queryset[0].user_id

    userlike,created = Userlikes.objects.get_or_create(company_id = company_id, liker_id = user_id, vehicle_id = vehicle_id)
    if not created:
        # the user already liked this picture before
        data = {
            'response':"data already exists"
        }

    else:
   
        data = {
            'response':"data stored"
        }
    return JsonResponse(data);

    # return render(request, 'registration/index.html', {})
def likecounterDecrement(request):

    instance    = request.user
    user_id     = instance.id

    vehicle_id  = request.GET.get('id', None)
    queryset    = Vehicles.objects.filter(id = vehicle_id)
    company_id  = queryset[0].user_id
    
    
    userquery = Userlikes.objects.filter(vehicle_id = vehicle_id, liker_id = user_id)
    userquery.delete()
   
    data = {
            'response':'data deleted'
       }

    
    return JsonResponse(data);


def validate_username(request):
    username = request.GET.get('username', None)
    data = {
        'is_taken': User.objects.filter(username=username).exists()
    }
    return JsonResponse(data)

def validate_email(request):
    email = request.GET.get('email', None)
    data = {
        'is_taken': Userprofile.objects.filter(email=email).exists()
    }
    return JsonResponse(data)

# def fetchLikeData(request):
#     queryset = Vehicles.objects.raw('''SELECT * from myapp_vehicles LEFT JOIN myapp_userlikes on myapp_vehicles.id = myapp_userlikes.vehicle_id and myapp_userlikes.liker_id = 15''')

def bubble_chart(request):
    return render(request, 'Automobile_sales/visualize.html', {})

def userprofile(request):
    return render(request, 'Automobile_sales/userprofile.html', {})
