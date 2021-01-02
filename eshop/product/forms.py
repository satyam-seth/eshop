from django import forms
from django.forms import fields
from django.http.response import HttpResponse, HttpResponseRedirect
from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model=Product
        # fields='__all__'
        exclude=('seller',)