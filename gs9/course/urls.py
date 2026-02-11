from django.urls import path
from . import views

urlpatterns = [
    path('dj_cor/', views.learn_django),
    path('py_fe/', views.learn_python),
]