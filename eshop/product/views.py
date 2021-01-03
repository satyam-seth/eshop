from django.shortcuts import render,redirect
from django.views import View
from django.views.generic import ListView
from django.contrib.auth.models import User
from .forms import ProductForm
from .models import Product
from core.models import Profile

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
            new_product=Product(seller=self.request.user,title=title,date=date,description=description,mrp=mrp,selling_price=selling_price,location=self.request.user.profile.city)
            new_product.save()
            return redirect('dashboard')



class ShowProduct(ListView):
    model=Product
    template_name='product/products.html'
    context_object_name='products'
    
    def get_queryset(self):
        return Product.objects.filter(location=self.request.user.profile.city)

    def get_context_data(self,*args,**kwargs):
        context=super().get_context_data(*args,**kwargs)
        context['products_active']='active'
        context['products_disabled']='disabled'
        return context