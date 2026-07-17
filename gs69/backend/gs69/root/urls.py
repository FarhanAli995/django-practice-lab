from django.urls import path
from . import views

urlpatterns = [
    # Home page with form and list
    path('', views.home, name='home'),
    
    # Dashboard
    path('dashboard/', views.dashboard, name='dashboard'),
    
    # Profile CRUD
    path('profiles/', views.profile_list, name='profile_list'),
    path('profiles/create/', views.profile_create, name='profile_create'),
    path('profiles/<int:pk>/', views.profile_detail, name='profile_detail'),
    path('profiles/<int:pk>/update/', views.profile_update, name='profile_update'),
    path('profiles/<int:pk>/delete/', views.profile_delete, name='profile_delete'),
]
