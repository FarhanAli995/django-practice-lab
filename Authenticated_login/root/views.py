from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from .forms import RegistrationForm


def home(request):
    return render(request, 'root/home.html')


def register_view(request):
    """
    Handles user registration.
    On success, creates the user, logs them in, and redirects to the home page.
    """
    # Prevent logged-in users from accessing the registration page
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            # Save the user to the database
            user = form.save()
            
            # Log the user in immediately after successful signup
            # Specify the backend to avoid Multiple Authentication Backends errors
            login(request, user, backend='django.contrib.auth.backends.ModelBackend')
            
            messages.success(request, f"Account created successfully! Welcome, {user.first_name}.")
            return redirect('home')  # Replace 'home' with your actual URL name
        else:
            messages.error(request, "Please correct the errors below.")
    else:
        form = RegistrationForm()

    return render(request, 'root/signup.html', {'form': form})


def signup_view(request):
    return register_view(request)


def login_view(request):
    """
    Handles user login.
    Upon successful login, the signal in models.py automatically fires 
    and saves the user's IP and timestamp to the LoginHistory model.
    """
    # Prevent logged-in users from accessing the login page
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('username') # AuthenticationForm maps the USERNAME_FIELD to 'username'
            password = form.cleaned_data.get('password')
            
            # Authenticate the user
            user = authenticate(request, email=email, password=password)
            
            if user is not None:
                login(request, user) # <--- THIS triggers the log_user_login signal in models.py
                messages.success(request, f"You are now logged in as {user.first_name}.")
                return redirect('home')
            else:
                messages.error(request, "Invalid email or password.")
        else:
            messages.error(request, "Invalid email or password.")
    else:
        form = AuthenticationForm()

    return render(request, 'root/login.html', {'form': form})


def logout_view(request):
    """
    Handles user logout.
    """
    logout(request)
    messages.info(request, "You have successfully logged out.")
    return redirect('login')