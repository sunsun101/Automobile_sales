from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from .models import Userprofile
from .models import Vehicles




def index(request):
	return render(request, 'registration/index.html', { })

def home(request):
	
    instance = request.user
    userid   = instance.id
    queryset = Vehicles.objects.filter(user_id = userid)
    return render(request,"Automobile_sales/home.html",{'queryset': queryset })

def user_logout(request):
    logout(request)
    return render(request, "registration/index.html", { })

def Register(request):
	return render(request,"registration/register.html", {})

def user_login(request):
    username = request.POST['name']
    password = request.POST['psw']
    
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            login(request,user)
            instance = request.user
            userid   = instance.id
            queryset = Vehicles.objects.filter(user_id = userid)
            return HttpResponseRedirect('/home/')
            
        else:
            return render(request, 'registration/index.html', {'error': True })
    else:
        return render(request, 'registration/index.html', {'error': True })

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
    return render(request,'Automobile_sales/Vehicle_upload.html', {})

# @login_required
# @transaction.atomic
# def update_profile(request):
#     if request.method == 'POST':
#         user_form = UserForm(request.POST, instance=request.user)
#         profile_form = ProfileForm(request.POST, instance=request.user.profile)
#         if user_form.is_valid() and profile_form.is_valid():
#             user_form.save()
#             profile_form.save()
#             messages.success(request, _('Your profile was successfully updated!'))
#             return redirect('settings:profile')
#         else:
#             messages.error(request, _('Please correct the error below.'))
#     else:
#         user_form = UserForm(instance=request.user)
#         profile_form = ProfileForm(instance=request.user.profile)
#     return render(request, 'profiles/profile.html', {
#         'user_form': user_form,
#         'profile_form': profile_form
#     })

def vehicle_store(request):
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



