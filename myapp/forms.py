from django import forms

from django.forms import ModelForm
from . models import Userprofile


class ProfileForm(ModelForm):
    class Meta:
        model = Userprofile
        fields = ['username','password']
        widgets = {
                    'password': forms.PasswordInput(),
                  }