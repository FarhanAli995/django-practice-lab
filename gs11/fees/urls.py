from django.urls import path
from . import views

urlpatterns = [
    path('fee_dj/', views.dj_fee),
    path('fee_py/', views.py_fee),
]