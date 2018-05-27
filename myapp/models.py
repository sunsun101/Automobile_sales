from django.db import models
from django import forms
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.validators import MinValueValidator, MaxValueValidator

class Userprofile(models.Model):
	# user = models.OneToOneField(User, on_delete=models.CASCADE ,null=True)
	# password 	= models.CharField(max_length=100,blank=False)
	first_name	= models.CharField(max_length=50,blank=True)
	middle_name	= models.CharField(max_length=50,blank=True)
	last_name	= models.CharField(max_length=50,blank=True)
	gender 		= models.CharField(max_length=10,blank=True)
	email		= models.CharField(max_length=100,null=True)
	birth_date	= models.DateField(null=True,blank=True)
	user_name   = models.CharField(max_length=30,blank=True)
	password 	= models.CharField(max_length=16,blank=True)
	Acc_type	= models.CharField(max_length= 10,default = "individual") 

	# @receiver(post_save,sender=User)
	# def create_user_profile(sender, instance, created, **kwargs):
	# 	if created:
	# 		Userprofile.objects.create(user=instance)

	# @receiver(post_save, sender=User)
	# def save_user_profile(sender, instance, **kwargs):
	# 	instance.userprofile.save()
	
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

	def __str__(self):
    		return self.vehicle_type