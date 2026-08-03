from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm, UserCreationForm
from django.contrib.auth.views import PasswordChangeView
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required

# ==========================================
# 1. LOGOUT VIEW
# ==========================================
def custom_logout_view(request):
    """Custom logout view that logs out user and redirects to login"""
    if request.method == 'POST':
        logout(request)
        messages.info(request, '✅ Aap successfully logout ho gaye hain!')
        return redirect('login')
    return redirect('profile')


# ==========================================
# 2. PROFILE VIEW
# ==========================================
@login_required
def profile_view(request):
    """User profile dashboard with links to change password"""
    return render(request, 'login/profile.html')


# ==========================================
# 2. LOGIN VIEW (Aapka custom code)
# ==========================================
def custom_login_view(request):
    if request.method == 'POST':
        u_name = request.POST.get('username')
        p_word = request.POST.get('password')

        user = authenticate(request, username=u_name, password=p_word)

        if user is not None:
            login(request, user)
            return redirect('profile')
        else:
            messages.error(request, "Username ya password galat hai! Dobara koshish karein.")

    return render(request, 'login/login.html')

# Registration View
def register_view(request):
    """User registration view using Django's built-in UserCreationForm"""
    if request.user.is_authenticated:
        return redirect('profile')

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, '✅ Aapka account kamyabi se ban gaya hai! Ab aap login kar sakte hain.')
            return redirect('login')
        else:
            messages.error(request, '❌ Kuch galat ho gaya. Dobara koshish karein.')
    else:
        form = UserCreationForm()

    return render(request, 'login/register.html', {'form': form})


# ==========================================
# PASSWORD CHANGE VIEW (With LoginRequiredMixin)
# ==========================================

class MyPasswordChangeView(LoginRequiredMixin, PasswordChangeView):
    """
    Password change view that requires user to be logged in.
    User must provide old password, new password, and confirmation.
    """
    form_class = PasswordChangeForm
    template_name = 'login/password_change.html'
    success_url = reverse_lazy('password_change_done')
    
    def form_valid(self, form):
        """Called when valid form data has been POSTed."""
        # Save the new password
        form.save()
        
        # Important: Update session to prevent user from being logged out
        update_session_auth_hash(self.request, form.user)
        
        # Success message
        messages.success(self.request, 'Aapka password kamyabi se change ho gaya hai!')
        
        return super().form_valid(form)
    
    def form_invalid(self, form):
        """Called when invalid form data has been POSTed."""
        messages.error(self.request, '❌ Kuch galat ho gaya. Dobara koshish karein.')
        return super().form_invalid(form)