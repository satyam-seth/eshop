from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm,UsernameField,UserCreationForm
from django.utils.translation import gettext_lazy as _
from .models import Profile

class LoginForm(AuthenticationForm):
    username=UsernameField(widget=forms.TextInput(attrs={'autofocus':True,'class':'form-control','placeholder':'enter your username'}))
    password = forms.CharField(
        label=_("Password"),
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'current-password','class':'form-control','placeholder':'enter your password'}),
    )

class SignUpForm(UserCreationForm):
    password1=forms.CharField(label='Password:',widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'enter password'}))
    password2=forms.CharField(label='Confirm Password:',widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'re-enter password'}))
    class Meta:
        model=User
        fields=['username','first_name','last_name','email']
        labels={'first_name':'First Name','last_name':'Last Name','email':'Email'}
        widgets={
            'username':forms.TextInput(attrs={'class':'form-control','placeholder':'enter username'}),
            'first_name':forms.TextInput(attrs={'class':'form-control','placeholder':'enter first name'}),
            'last_name':forms.TextInput(attrs={'class':'form-control','placeholder':'enter last name'}),
            'email':forms.EmailInput(attrs={'class':'form-control','placeholder':'enter email id'}),
        }

class ProfileForm(forms.ModelForm):
    account_type=forms.ChoiceField(choices=(('customer','Customer'),('seller','Seller')),widget=forms.Select(attrs={'class':'form-select'}))
    class Meta:
        model=Profile
        fields=['phone','city']
        widgets={
            'phone':forms.TextInput(attrs={'class':'form-control','placeholder':'enter phone number','pattern':'^\d{10}$'}),
            'city':forms.TextInput(attrs={'class':'form-control','placeholder':'enter city name'}),
        }