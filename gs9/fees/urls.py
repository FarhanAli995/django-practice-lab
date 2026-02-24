from django.urls import path
from . import views

urlpatterns = [
    path('fees_dj/', views.fees_django),
    path('fees_py/', views.fees_python),
]
