from django.urls import path
from store import views


app_name = 'store'
urlpatterns = [
    path('', views.store, name='store'),
    path('cart/', views.cart, name='cart'),
    path('detail/<int:pk>/', views.detail, name='detail'),
    path('checkout/', views.checkout, name='checkout')
]

