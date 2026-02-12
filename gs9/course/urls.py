from django.urls import path
from . import views

urlpatterns = [
    path('dj_cor/', views.learn_django),
    path('py_cor/', views.learn_python),
]