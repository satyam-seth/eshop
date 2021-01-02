from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm,UsernameField,UserCreationForm
from django.utils.translation import gettext_lazy as _
from phonenumber_field.formfields import PhoneNumberField
from .models import Profile

class LoginForm(AuthenticationForm):
    username=UsernameField(widget=forms.TextInput(attrs={'autofocus':True}))
    password = forms.CharField(
        label=_("Password"),
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'current-password'}),
    )

class SignUpForm(UserCreationForm):
    password2=forms.CharField(label='Confirm Password:',widget=forms.PasswordInput)
    # phone=PhoneNumberField()
    # city=forms.CharField(widget=forms.TextInput(attrs={}))
    class Meta:
        model=User
        fields=['username','first_name','last_name','email']
        labels={'email':'Email'}

class ProfileForm(forms.ModelForm):
    account_type=forms.ChoiceField(choices=(('customer','customer'),('seller','seller')))
    class Meta:
        model=Profile
        fields=['phone','city']