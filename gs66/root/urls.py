from django.urls import path
from . import views
from django.contrib import admin

# In root/urls.py
urlpatterns = [
    path('', views.home_view, name='home'), # You'll need to create a home_view in views.py
    path('students/<int:my_id>/', views.stu_details, name='details'),   
]

 
