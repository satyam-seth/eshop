from django.shortcuts import render,redirect
from django.views import View
from .forms import ProductForm
from .models import Product

# Create your views here.

class AddProduct(View):
    def get(self,request):
        form=ProductForm()
        return render(request,'product/add.html',{'form':form})

    def post(self,request):
        form=ProductForm(request.POST)
        if form.is_valid():
            title=form.cleaned_data['title']
            date=form.cleaned_data['date']
            description=form.cleaned_data['description']
            mrp=form.cleaned_data['mrp']
            selling_price=form.cleaned_data['selling_price']
            new_product=Product(seller=self.request.user,title=title,date=date,description=description,mrp=mrp,selling_price=selling_price)
            new_product.save()
            return redirect('dashboard')