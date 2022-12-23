from django.contrib import admin
from django.urls import path,include
from django.contrib.auth import views
from . import views as user_view
urlpatterns = [
    path('',views.LoginView.as_view(template_name='users/login.html'),name='login'),
    path('profile/',user_view.profile,name='profile'),
    path('logout/',views.LogoutView.as_view(template_name='users/logout.html'),name='logout'),
    path('register/',user_view.register,name='register'),
]