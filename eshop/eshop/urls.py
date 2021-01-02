from django.contrib import admin
from django.urls import path,include
from core import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.HomeView.as_view(),name='home'),
    path('login/', views.UserLoginView.as_view(),name='login'),
    path('logout/', views.UserLogoutView.as_view(),name='logout'),
    path('signup/', views.UserSignUpView.as_view(),name='signup'),
    path('dashboard/', views.DashboardView.as_view(),name='dashboard'),
    path('product/',include('product.urls')),
]