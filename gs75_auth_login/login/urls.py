from django.urls import path
from django.contrib.auth import views as auth_views
from .forms import CustomLoginForm
from . import views

urlpatterns = [
    path('', auth_views.LoginView.as_view(
        template_name='login/login.html',
        authentication_form=CustomLoginForm
    ), name='login'),

    # Reset Password URLs (Built-in)
    path('reset_password/', auth_views.PasswordResetView.as_view(template_name='login/reset_pass.html'), name='password_reset'),
    path('password_reset_done/', auth_views.PasswordResetDoneView.as_view(template_name='login/password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='login/password_reset_confirm.html'), name='password_reset_confirm'),
    path('reset_done/', auth_views.PasswordResetCompleteView.as_view(template_name='login/reset_pass_complete.html'), name='password_reset_complete'),

    # Registration URL (New)
    path('register/', views.register_view, name='register'),

    # Change Password URLs (Requires Old Password)
    path('change_password/', auth_views.PasswordChangeView.as_view(
        template_name='login/password_change.html', 
        success_url='/password_change_done/'
    ), name='password_change'),
    
    path('password_change_done/', auth_views.PasswordChangeDoneView.as_view(
        template_name='login/password_change_done.html'
    ), name='password_change_done'),
]