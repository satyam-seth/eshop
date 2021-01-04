from django.urls import path
from . import views

urlpatterns=[
    path('',views.ShowProductView.as_view(),name='products'),
    path('add/',views.AddProductView.as_view(),name='add'),
    path('edit/<int:pk>/',views.UpdateProductView.as_view(),name='edit'),
]