from django.db import models
from django import forms

class Userprofile(models.Model):
	user_name 	= models.CharField(max_length=100,blank=False)
	password 	= models.CharField(max_length=100,blank=False)
	first_name	= models.CharField(max_length=50,blank=True)
	middle_name	= models.CharField(max_length=50,blank=True)
	last_name	= models.CharField(max_length=50,blank=True)
	gender 		= models.CharField(max_length=10,blank=True)
	email		= models.CharField(max_length=100,null=True)
	birth_date	= models.DateField(null=True,blank=True)

	

	def __str__(self):
    		return self.user_name

class Vehicles(models.Model):
	image = models.ImageField(upload_to="vehicle_image")