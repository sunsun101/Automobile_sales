from django import forms

from django.forms import ModelForm
from . models import Userprofile

class UserForm(forms.ModelForm):
	class Meta:
		model = User
		fields = ('first_name','last_name','email')

