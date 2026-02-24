from django.urls import path
from . import views

urlpatterns = [
    path('learn_dj/', views.learn_dj),
    path('learn_py/', views.learn_py),
]