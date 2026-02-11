from django.urls import path
from StudentFee import views

urlpatterns= [
    path('StudentFee/', views.StudentFee,name='StudentFee'),
    path('firstYearStu/', views.firstYearStu,name='firstYearStu'),
]