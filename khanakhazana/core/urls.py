from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='home'),  
    path('ab/', views.about, name='about'),
    path('foot/', views.footer, name='footer'),
    path('menu/', views.menu, name='menu'),
]