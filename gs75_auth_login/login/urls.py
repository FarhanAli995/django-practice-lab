from django.urls import path
from django.contrib.auth import views as auth_views
from .forms import CustomLoginForm
from . import views

urlpatterns = [
    # Login URLs (both root and /login/ work)
    path('', auth_views.LoginView.as_view(
        template_name='login/login.html',
        authentication_form=CustomLoginForm
    ), name='login'),
    path('login/', auth_views.LoginView.as_view(
        template_name='login/login.html',
        authentication_form=CustomLoginForm
    )),

    # Logout URL (Custom view for better handling)
    path('logout/', views.custom_logout_view, name='logout'),

    # Profile URL
    path('profile/', views.profile_view, name='profile'),

    # Reset Password URLs (Built-in)
    path('reset_password/', auth_views.PasswordResetView.as_view(template_name='login/reset_pass.html'), name='password_reset'),
    path('password_reset_done/', auth_views.PasswordResetDoneView.as_view(template_name='login/password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='login/password_reset_confirm.html'), name='password_reset_confirm'),
    path('reset_done/', auth_views.PasswordResetCompleteView.as_view(template_name='login/reset_pass_complete.html'), name='password_reset_complete'),

    # Registration URL (New)
    path('register/', views.register_view, name='register'),

    # Change Password URLs (Requires Old Password)
    # Using custom view with LoginRequiredMixin protection
    path('change_password/', views.MyPasswordChangeView.as_view(), name='password_change'),
    
    path('password_change_done/', auth_views.PasswordChangeDoneView.as_view(
        template_name='login/password_change_done.html'
    ), name='password_change_done'),
]