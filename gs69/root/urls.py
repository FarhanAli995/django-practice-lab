from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("edit/<int:id>/", views.edit_user, name="edit_user"),
    path("delete/<int:id>/", views.delete_user, name="delete_user"),
]
