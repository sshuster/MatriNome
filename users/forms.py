from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile


class UserRegisterForm(UserCreationForm):
	email = forms.EmailField()
	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2']


class UserUpdateForm(forms.ModelForm):
	email = forms.EmailField()

	class Meta:
		model = User
		fields = ['username', 'email']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['name','mobile_no', 'image','dob', 'gender','address','state', 'city', 'bio', 'interests']
        widgets = {
            'interests': forms.widgets.CheckboxSelectMultiple,
        }

class AddInterestForm(forms.Form):
    add_interest = forms.CharField(label = 'Other Interests',max_length = 100 ,required = False) 