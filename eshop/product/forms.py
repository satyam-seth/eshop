from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model=Product
        exclude=('seller','date','location')
        widgets={
            'title':forms.TextInput(attrs={'class':'form-control','placeholder':'enter product title'}),
            'description':forms.Textarea(attrs={'class':'form-control','placeholder':'enter product description','rows':5}),
            'mrp':forms.NumberInput(attrs={'class':'form-control','min':'0','max':'1000000','placeholder':'enter product mrp'}),
            'selling_price':forms.NumberInput(attrs={'class':'form-control','min':'0','max':'1000000','placeholder':'enter product selling price'})
        }