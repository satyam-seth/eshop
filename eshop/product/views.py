from django.shortcuts import render,redirect
from django.utils.timezone import localtime, now
from django.views import View
from django.views.generic import ListView
from .forms import ProductForm
from .models import Product
from django.contrib.auth.models import Group
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required,user_passes_test
from django.views.generic.edit import UpdateView
# Create your views here.

@method_decorator(login_required,name='dispatch')
class ShowProductView(ListView):
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

@method_decorator(user_passes_test(lambda u: Group.objects.get(name='seller') in u.groups.all()),name='dispatch')
class AddProductView(View):
    def get(self,request):
        form=ProductForm()
        return render(request,'product/add.html',{'form':form})

    def post(self,request):
        form=ProductForm(request.POST)
        if form.is_valid():
            title=form.cleaned_data['title']
            description=form.cleaned_data['description']
            mrp=form.cleaned_data['mrp']
            selling_price=form.cleaned_data['selling_price']
            new_product=Product(seller=self.request.user,title=title,date=localtime(now()).date(),description=description,mrp=mrp,selling_price=selling_price,location=self.request.user.profile.city)
            new_product.save()
            return redirect('dashboard')

@method_decorator(user_passes_test(lambda u: Group.objects.get(name='seller') in u.groups.all()),name='dispatch')
class UpdateProductView(UpdateView):
    model=Product
    form_class=ProductForm
    template_name='product/edit.html'
    success_url='/dashboard/'