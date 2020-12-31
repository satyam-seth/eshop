from django.contrib import admin
from django.urls import path
from core import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.HomeView.as_view(),name='home'),
    path('login/', views.UserLoginView.as_view(),name='login'),
    path('logout/', views.UserLogoutView.as_view(),name='logout'),
]