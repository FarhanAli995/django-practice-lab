from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages

def custom_login_view(request):
    if request.method == 'POST':
        u_name = request.POST.get('username')
        p_word = request.POST.get('password')

        # 1. Django check karega ke user exist karta hai aur password sahi hai ya nahi
        user = authenticate(request, username=u_name, password=p_word)

        if user is not None:
            # 2. User sahi hai -> Login karayein aur Profile page par bhej dein
            login(request, user)
            return redirect('profile')
        else:
            # 3. Username/Password galat hone par error message set karein
            messages.error(request, "Username ya password galat hai! Dobara koshish karein.")

    return render(request, 'login/login.html')