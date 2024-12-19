from django.contrib import admin
from django.urls import path,include
from home import views


urlpatterns = [
    path('', views.index, name='home'),
    path('register', views.register, name='register'),
    path('login', views.userlogin, name='login'),
    path('logout/', views.userlogout, name='logout'),
    path('delete/<str:name>/', views.tododelete, name='delete'),
    path('update/<str:name>/', views.todoupdate, name='update'),

]