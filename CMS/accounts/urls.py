from django.urls import path

from .import views

urlpatterns = [
    path('register/', views.registerPage, name='register'),
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutUser, name='logout'),

    path('',views.home, name='home'),
    path('user/', views.userPage, name='user'),
    path('products/',views.products, name='products'),
    path('customer/<str:pk_test>/',views.customer, name='customer'),
    path('created_order/<str:pk>/', views.createdOrder, name='created_order'),
    path('update_order/<str:pk>/', views.updateOrder, name='update_order'),
    path('delete_order/<str:pk>/', views.deleteOrder, name='delete_order'),



]