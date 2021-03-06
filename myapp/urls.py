from django.conf.urls import include, url
from . import views
from django.contrib.auth import views as auth_views



urlpatterns = [
	

	url(r'^logout/$', views.user_logout, name='logout'),
	url(r'^home/$', views.home, name='home'),
	url(r'^adminpage/$', views.adminpage, name='adminpage'),
	url(r'^$',views.index,name='index'),
	url(r'^login/$',views.user_login, name='login'),
	url(r'^Upload/$',views.vehicle_upload, name='Vehicle_upload'),
	url(r'^Register/$',views.Register, name='Register'),
	url(r'^signup/$',views.signup, name='Signup'),
	url(r'^create_account/$',views.create_account, name='create_account'),
	url(r'^vehicle_store/$',views.vehicle_store, name='vehicle_store'),
	url(r'^userhome/$',views.userhome, name='userhome'),
	url(r'^likecounterIncrement/$',views.likecounterIncrement, name='likecounterIncrement'),
	url(r'^likecounterDecrement/$',views.likecounterDecrement, name='likecounterDecrement'),
	url(r'^dislikecounterDecrement/$',views.dislikecounterDecrement, name='dislikecounterDecrement'),
	url(r'^dislikecounterIncrement/$',views.dislikecounterIncrement, name='dislikecounterIncrement'),
	url(r'^validate_username/$',views.validate_username, name='validate_username'),
	url(r'^validate_email/$',views.validate_email, name='validate_email'),
	url(r'^userprofile/$',views.userprofile, name='userprofile'),
	url(r'^bubble_chart/$',views.bubble_chart, name='bubble_chart'),
	url(r'^bar_chart/$',views.bar_chart, name='bar_chart'),
	url(r'^line_chart/$',views.line_chart, name='line_chart'),
	url(r'^detailPage/$',views.detailPage, name='detailPage'),
	url(r'^email/$',views.email, name='email'),
	url(r'^transferEmail/$',views.transferEmail, name='transferEmail'),

	


		

    
    ]