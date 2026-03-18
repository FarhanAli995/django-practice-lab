from django.urls import path
from . import views

urlpatterns = [
    path('', views.stud_data, name='stud_data'),
    path('te/', views.teachers, name="teachers")
]