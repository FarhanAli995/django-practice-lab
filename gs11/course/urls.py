from django.urls import path
from . import views

urlpatterns = [
    path('learn_dj/', views.learn_django),
    path('learn_py/', views.learn_python),
]