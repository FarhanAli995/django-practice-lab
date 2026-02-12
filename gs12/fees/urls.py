from django.urls import path
from . import views

urlpatterns = [
    path('fees_dj/', views.fees_dj),
    path('fees_py/', views.fees_py),
]