from django.shortcuts import render,redirect
from django.views.generic import TemplateView
from django.views.generic.list import ListView
from django.views import View
from django.contrib.auth.views import LoginView,LogoutView
from django.contrib.auth.models import User,Group
from django.contrib.auth import authenticate,login
from .forms import LoginForm,ProfileForm,SignUpForm
from .models import Profile
from product.models import Product
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import user_passes_test

# Create your views here.

class HomeView(TemplateView):
    template_name='core/home.html'

    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context['home_active']='active'
        context['home_disabled']='disabled'
        return context

@method_decorator(user_passes_test(lambda u: Group.objects.get(name='seller') in u.groups.all()),name='dispatch')
class DashboardView(ListView):
    model=Product
    template_name='core/dashboard.html'
    context_object_name='products'
    
    def get_queryset(self):
        return Product.objects.filter(seller=self.request.user)

    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context['dashboard_active']='active'
        context['dashboard_disabled']='disabled'
        return context

class UserLoginView(LoginView):
    template_name='core/login.html'
    authentication_form=LoginForm

    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context['login_active']='active'
        context['login_disabled']='disabled'
        return context

class UserLogoutView(LogoutView):
    template_name='core/home.html'

    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context['home_active']='active'
        context['home_disabled']='disabled'
        return context

class UserSignUpView(View):
    def get(self,request):
        user_form=SignUpForm()
        profile_form=ProfileForm()
        context={
            'user_form':user_form,
            'profile_form':profile_form,
            'signup_active':'active',
            'signup_disabled':'disabled',
            }
        return render(request,'core/signup.html',context)
    
    def post(self,request):
        user_form=SignUpForm(request.POST)
        profile_form=ProfileForm(request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            username=user_form.cleaned_data['username']
            first_name=user_form.cleaned_data['first_name']
            last_name=user_form.cleaned_data['last_name']
            email=user_form.cleaned_data['email']
            password=user_form.cleaned_data['password1']
            phone=profile_form.cleaned_data['phone']
            city=profile_form.cleaned_data['city']
            account_type=profile_form.cleaned_data['account_type']
            newuser=User.objects.create_user(username=username,first_name=first_name,last_name=last_name,email=email,password=password)
            newuser.save()
            group=Group.objects.get(name=account_type)
            newuser.groups.add(group)
            profile=Profile.objects.create(user=newuser,phone=phone,city=city.lower())
            profile.save()
            user=authenticate(username=username,password=password)
            if user is not None:
                login(request,user)
        return redirect('home')