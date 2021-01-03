from django.urls import path
from . import views

urlpatterns=[
    path('add/',views.AddProduct.as_view(),name='add'),
    path('',views.ShowProduct.as_view(),name='products'),
]