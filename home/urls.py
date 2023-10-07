from django.contrib import admin
from django.urls import path
from home import views

admin.site.site_header = "Super User Admin - Abhijeet"
admin.site.site_title = "Super-User Portal"
admin.site.index_title = "Welcome to Super-User Portal"

urlpatterns = [
    path('', views.index, name='home'),
    path('login', views.loginUser, name='login'),
    path('logout', views.logoutUser, name='logout'),
]
