from django.urls import path
from users import views as user_views
from . import views
urlpatterns = [
  path('home/',views.home_page,name='blog-home'),
  path('about/',views.about_page,name='blog-about'),
]