from django.conf.urls import include, url
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
	
	# url(r'^login/$', views.user_login, name='login'),
	url(r'^logout/$', views.user_logout, name='logout'),
	url(r'^home/', 'myapp.views.home', name='home'),
	url(r'^$',views.index,name='index'),
	url(r'^login/$',views.user_login, name='login'),
    
        
    ]
