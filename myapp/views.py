from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from .models import Userprofile
from .models import Vehicles,Userlikes
from django.http import JsonResponse
from django.db.models import F
import datetime
from pprint import pprint
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from Automobile_sales import helpers
from myapp import sendEmail




def index(request):
	return render(request, 'registration/index.html', { })

def home(request):
    if not request.session.get('logged_in'):
        return HttpResponseRedirect('/')
    instance = request.user
    userid   = instance.id
    queryset = Vehicles.objects.filter(user_id = userid)

    userdetail = User.objects.filter(id = userid)
    username   = userdetail[0].username

    userdetail2 = Userprofile.objects.filter(user_name = username)
    if userdetail2[0].Acc_type == 'C':

        return render(request,"Automobile_sales/home.html",{'queryset': queryset, 'home': True,'userid':userid})
    else:
        return render(request,"Automobile_sales/home.html",{'queryset': queryset, 'individual_home': True,'userid':userid})




def userhome(request):
    if not request.session.get('logged_in'):
        return HttpResponseRedirect('/')
    instance = request.user
    userid   = instance.id
    queryset = Vehicles.objects.raw('''SELECT * from myapp_vehicles LEFT JOIN myapp_userlikes on myapp_vehicles.id = myapp_userlikes.vehicle_id and myapp_userlikes.liker_id = %s ''', [userid])
    paginator = Paginator(queryset,5)
    paginator._count = len(list(queryset))
    page = request.GET.get('page')

    try:
        # create Page object for the given page
        queryset = paginator.page(page)
    except PageNotAnInteger:
        # if page parameter in the query string is not available, return the first page
        queryset = paginator.page(1)
    except EmptyPage:
        # if the value of the page parameter exceeds num_pages then return the last page
        queryset = paginator.page(paginator.num_pages)
    

    return render(request,"Automobile_sales/userhome.html",{'queryset': queryset,'userhomepage': True,'userid':userid})

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
    instance = request.user
    userid   = instance.id
    
    userdetail = User.objects.filter(id = userid)
    username   = userdetail[0].username

    userdetail2 = Userprofile.objects.filter(user_name = username)
    if userdetail2[0].Acc_type == 'C':

        return render(request,'Automobile_sales/Vehicle_upload.html', {'company':True})
    else:
        return render(request,'Automobile_sales/Vehicle_upload.html', {'company':False,'individual_home':True})



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

    check       = Userlikes.objects.filter(company_id = company_id, liker_id = user_id, vehicle_id = vehicle_id)
    if check:
        if check[0].rating == -1:
            Userlikes.objects.filter(company_id = company_id, liker_id = user_id, vehicle_id = vehicle_id).update(rating = 1)
            data = {
                'response':"data updated"
            }
    else:

        userlike,created = Userlikes.objects.get_or_create(company_id = company_id, liker_id = user_id, vehicle_id = vehicle_id, rating = 1)
        like_store = Vehicles.objects.filter(id = vehicle_id).update(like_count = F('like_count')+1)
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
    like_store = Vehicles.objects.filter(id = vehicle_id).update(like_count = F('like_count')-1)
   
    data = {
            'response':'data deleted'
       }

    
    return JsonResponse(data);

def dislikecounterDecrement(request):

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

def dislikecounterIncrement(request):

    instance    = request.user
    user_id     = instance.id

    vehicle_id  = request.GET.get('id', None)
    queryset    = Vehicles.objects.filter(id = vehicle_id)
    company_id  = queryset[0].user_id

    check       = Userlikes.objects.filter(company_id = company_id, liker_id = user_id, vehicle_id = vehicle_id)
    if check:
        if check[0].rating == 1:
            Userlikes.objects.filter(company_id = company_id, liker_id = user_id, vehicle_id = vehicle_id).update(rating = -1)
            data = {
                'response':"data updated"
            }
    else:
        userlike,created = Userlikes.objects.get_or_create(company_id = company_id, liker_id = user_id, vehicle_id = vehicle_id, rating = -1)
        if not created:
        # the user already disliked this picture before
            data = {
                'response':"data already exists"
            }

        else:
   
            data = {
                'response':"data stored"
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
    # if not request.session.get('logged_in'):
    #     return HttpResponseRedirect('/')
       
    # instance    = request.user
    # company_id     = instance.id
    # queryset = Userlikes.objects.raw('''SELECT * from myapp_userlikes LEFT JOIN myapp_userprofile on myapp_userlikes.liker_id = myapp_userprofile.id and myapp_userlikes.company_id = %s''', [company_id])
    
    # age = [0]*4

    # for obj in queryset:
    #     if obj.birth_date:
    #         calc_age = datetime.date.today()-obj.birth_date
    #         if calc_age > 17 and calc_age < 31:
    #         young = obj

    #         elif calc_age>30 and calc_age<51:
    #         middle = obj

    #         elif calc_age>50 and calc_age<71:
    #         old = obj

    #         else:
    #         veryold = obj

    # x=0
    # for y in young:
    #     length = len(list(young))
    #     yvehicleId = [0]*length
    #     ylike_rate = [0]*length
    #     ylike_count = [0]*length
    #     if x == 0:
    #         yvehicleId[x] = y.vehicle_id
    #         ylike_count[x] = like_count[x]+1
    #         x = x + 1


    #     elif x != 0:
    #         i = 0
    #         for i in range(0,length):
    #             if y.vehicle_id == yvehicleId[i]:
    #                 ylike_count[i] = ylike_count[i] + 1

    #         if i == 0:
    #             yvehicleId[x] = y.vehicle_id
    #             ylike_count[x] = ylike_count[x]+1
    #             x = x + 1


    return render(request, 'Automobile_sales/bubble_chart.html', {'company':True})

def bar_chart(request):
    if not request.session.get('logged_in'):
        return HttpResponseRedirect('/')
    instance    = request.user
    company_id     = instance.id
    if request.POST:
        year = request.POST.get('year')

        queryset = Userlikes.objects.raw('''SELECT * from myapp_userlikes LEFT JOIN myapp_userprofile on myapp_userlikes.liker_id = myapp_userprofile.id and myapp_userlikes.company_id = %s''', [company_id])
        male_count = [0] * 13
        female_count = [0] * 13
        other_count = [0] * 13
        male_percent = [0] * 13
        female_percent = [0] * 13
        for obj in queryset:
            if obj.rating == 1:
                test = year
                if obj.date.year == int(year):
                
                    for x in range(1,12):
                    
                        
                        if obj.date.month == x:
                            if obj.gender:
                                if obj.gender == 'male':
                                    male_count[x] = male_count[x] + 1
                                elif obj.gender == 'female':
                                    female_count[x] = female_count[x] + 1
                                else:
                                    other_count[x] = other_count[x] + 1

        for x in range(1,12):
            if (male_count[x] != 0 or female_count[x] != 0 or other_count[x] != 0):
                male_percent[x] = round((float(male_count[x])/(male_count[x]+female_count[x]+other_count[x]))*100,2)
                female_percent[x] = round((float(female_count[x])/(male_count[x]+female_count[x]+other_count[x]))*100,2)
        return render(request, 'Automobile_sales/bar_chart.html', {'company':True, 'male_percent':male_percent,'female_percent':female_percent})


    else:
        queryset = Userlikes.objects.raw('''SELECT * from myapp_userlikes LEFT JOIN myapp_userprofile on myapp_userlikes.liker_id = myapp_userprofile.id and myapp_userlikes.company_id = %s''', [company_id])
        male_count = [0] * 13
        female_count = [0] * 13
        other_count = [0] * 13
        male_percent = [0] * 13
        female_percent = [0] * 13
        for obj in queryset:
            if obj.rating == 1:
                if obj.date.year == datetime.datetime.now().year:
                    
                    for x in range(1,12):
                    
                        if obj.date.month == x:
                            if obj.gender:
                                if obj.gender == 'male':
                                    male_count[x] = male_count[x] + 1
                                elif obj.gender == 'female':
                                    female_count[x] = female_count[x] + 1
                                else:
                                    other_count[x] = other_count[x] + 1

        for x in range(1,12):
            if (male_count[x] != 0 or female_count[x] != 0 or other_count[x] != 0):
                male_percent[x] = round((float(male_count[x])/(male_count[x]+female_count[x]+other_count[x]))*100,2)
                female_percent[x] = round((float(female_count[x])/(male_count[x]+female_count[x]+other_count[x]))*100,2)


        return render(request, 'Automobile_sales/bar_chart.html', {'company':True, 'male_percent':male_percent,'female_percent':female_percent})

def line_chart(request):
    if not request.session.get('logged_in'):
        return HttpResponseRedirect('/')
    instance    = request.user
    company_id  = instance.id
   
    vehicle1_likes = [0] * 13
    vehicle2_likes = [0] * 13
    vehicle1_rates = [0] * 13
    vehicle2_rates = [0] * 13
    
    if request.POST:
        # values = [0]*2
        values = request.POST.getlist('test')
        value1 = int(values[0])
        value2 = int(values[1])
        
        queryset = Userlikes.objects.raw('''SELECT * from myapp_userlikes where company_id = %s and vehicle_id in (%s,%s) and rating = 1''', [company_id,value1,value2])
    else:
        value1 = 41
        value2 = 42
        queryset = Userlikes.objects.raw('''SELECT * from myapp_userlikes where company_id = %s and vehicle_id in (%s,%s) and rating = 1''', [company_id,value1,value2])
    
    vehicle_list = Vehicles.objects.filter(user_id = company_id)

    for obj in queryset:
        if obj.date.year == datetime.datetime.now().year:

            for x in range(1,12):
                
                if obj.date.month == x:

                    if obj.vehicle_id == value1:
                        vehicle1_likes[x] = vehicle1_likes[x] + 1
                    else:
                        vehicle2_likes[x] = vehicle2_likes[x] + 1
    
    for x in range(1,12):
            if (vehicle1_likes[x] != 0 or vehicle2_likes[x] != 0):
                vehicle1_rates[x] = round((float(vehicle1_likes[x])/(vehicle1_likes[x]+vehicle2_likes[x]))*100,2)
                vehicle2_rates[x] = round((float(vehicle2_likes[x])/(vehicle1_likes[x]+vehicle2_likes[x]))*100,2)  
            elif(vehicle1_likes[x] == 0 and vehicle2_likes[x] == 0 ):
                vehicle1_rates[x] = 0
                vehicle2_rates[x] = 0
            elif(vehicle1_likes[x] == 0 and vehicle2_likes[x] != 0):
                vehicle1_rates[x] = 0
                vehicle2_rates[x] = 100
            else:
                vehicle1_rates[x] = 100
                vehicle2_rates[x] = 0           


    return render(request, 'Automobile_sales/line_chart.html', {'value1':value1,'value2':value2,'company':True,'vehicle_list':vehicle_list,'vehicle1_rates':vehicle1_rates,'vehicle2_rates':vehicle2_rates})

def userprofile(request):
    return render(request, 'Automobile_sales/userprofile.html', {})

def detailPage(request):
    vehicle_id  = request.GET.get('id', None)
    queryset = Vehicles.objects.filter(id = vehicle_id)

    return render(request, 'Automobile_sales/detailPage.html', {'queryset':queryset,'individual_home':True})
    


def email(request):
    return render(request, 'Automobile_sales/email.html', {'individual_home':True})

def transferEmail(request):
    if request.POST:
        email    = request.POST.get('email')
        pwd      = request.POST.get('password')
        subject  = request.POST.get('subject')
        message  = request.POST.get('message')

        value = sendEmail.send(email,pwd,subject,message)
        if value == 'success':
            alert = True
       

    return render(request, 'Automobile_sales/email.html', {'individual_home':True,'alert':alert})

