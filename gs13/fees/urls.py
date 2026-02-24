from django.urls import path 
from . import views

urlpatterns = [
    path('fees_dj/', views.fees_dj),
    path('fees_py/', views.fees_py),
    path('fees_3/', views.fees_3),
    path('fees_4/',views.fees_4),
]