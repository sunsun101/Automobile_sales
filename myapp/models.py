from django.db import models
from django import forms
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.validators import MinValueValidator, MaxValueValidator
import datetime

class Userprofile(models.Model):
	# user = models.OneToOneField(User, on_delete=models.CASCADE ,null=True)
	# password 	= models.CharField(max_length=100,blank=False)rue
	first_name	= models.CharField(max_length=50,blank=True)
	middle_name	= models.CharField(max_length=50,blank=True)
	last_name	= models.CharField(max_length=50,blank=True)
	company_name = models.CharField(max_length=50,blank=True)
	gender 		= models.CharField(max_length=10,blank=True)
	email		= models.CharField(max_length=100,null=True,blank=True)
	birth_date	= models.DateField(null=True,blank=True)
	user_name   = models.CharField(max_length=30,blank=True,unique=True)
	password 	= models.CharField(max_length=16,blank=True)
	Acc_type	= models.CharField(max_length= 10,default = "I") 
	user_image  = models.ImageField(upload_to ="user_image",null=True)

	
	def __str__(self):
    		return self.first_name

class Vehicles(models.Model):
	vehicle_type	= models.CharField(max_length = 20,blank=True)
	brand			= models.CharField(max_length = 20,blank=True)
	model_no		= models.CharField(max_length = 50,blank =True)
	engine_power	= models.CharField(max_length=20,blank = True)
	price			= models.IntegerField(blank = True, null = True)
	description		= models.TextField(blank = True)
	image 			= models.ImageField(upload_to="vehicle_image")
	# user_id			= models.ForeignKey('Userprofile',on_delete=models.CASCADE, blank = True, null = True)
	user_id			= models.IntegerField(blank = True, null = True)
	like_count		= models.IntegerField(blank=True,null=True)
	condition 		= models.CharField(blank=True,null=True,max_length=10)

	def __str__(self):
    		return self.vehicle_type


class Userlikes(models.Model):

	company_id	= models.IntegerField(blank=True,null=True)
	liker_id	= models.IntegerField(blank=True,null=True)
	vehicle_id	= models.IntegerField(blank=True,null=True)
	date 		= models.DateTimeField(auto_now_add=True, null=True)
	rating		= models.IntegerField(blank=True,null=True)
