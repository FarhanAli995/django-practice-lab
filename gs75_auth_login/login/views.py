from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib import messages

# Django ke built-in password reset views ko import karein
from django.contrib.auth import views as auth_views

# ==========================================
# 1. LOGIN VIEW (Aapka custom code)
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

# registration form

from django.contrib.auth.forms import UserCreationForm  
# <--- Ise import karein

# 1. Registration View (New)
def register_view(request):
    # Agar user pehle se logged-in hai tou usay profile par bhej dein
    if request.user.is_authenticated:
        return redirect('profile')

    if request.method == 'POST':
        fm = UserCreationForm(request.POST)
        if fm.is_valid():
            fm.save()  # Naya user database mein save ho jayega
            messages.success(request, 'Aapka account kamyabi se ban gaya hai! Ab aap login kar sakte hain.')
            return redirect('login')
    else:
        fm = UserCreationForm()

    return render(request, 'login/register.html', {'form': fm})


# ==========================================
# 2. FORGOT PASSWORD VIEWS (Added)
# ==========================================

# Step 1: User apna email dalega
def user_change_pass(request):
    fm = PasswordChangeForm(user = request.user)
    return render(request, 'login/reset_pass.html', {'form': fm})