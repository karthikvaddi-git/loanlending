from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from accounts.models import *
from django.forms import ModelForm
from django import forms

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('username','name','email','phone',)

class userintrest(ModelForm):
    class Meta:
        model = userprofile
        fields = ('intrests',)
        
class userprofiles(ModelForm):
    class Meta:
        model = userprofile
        fields = ('profileimage','description','location','intrests',)
