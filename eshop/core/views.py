from django.views.generic import TemplateView
from django.contrib.auth.views import LoginView,LogoutView
from .forms import LoginForm

# Create your views here.

class HomeView(TemplateView):
    template_name='core/home.html'

    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context['home_active']='active'
        context['home_disabled']='disabled'
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