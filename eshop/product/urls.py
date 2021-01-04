from django.urls import path
from . import views

urlpatterns=[
    path('',views.ProductListView.as_view(),name='products'),
    path('add/',views.AddProductView.as_view(),name='add'),
    path('edit/<int:pk>/',views.ProductUpdateView.as_view(),name='edit'),
    path('delete/<int:pk>/',views.ProductDeleteView.as_view(),name='delete'),
]