from django.urls import path
from django.contrib.auth import views as auth_views
from .forms import CustomLoginForm

urlpatterns = [
    path('', auth_views.LoginView.as_view(
        template_name='login/login.html',
        authentication_form=CustomLoginForm
    ), name='login'),
]