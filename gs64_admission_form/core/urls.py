from django.urls import path
from . import views

urlpatterns = [
    path("", views.admission_application, name="admission_application"),
    path("success/", views.success, name="admission_success"),
]
