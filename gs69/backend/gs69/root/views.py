from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.db.models import Count, Q
from .models import UserProfile
from .forms import UserProfileForm

def home(request):
    """Home page with form and profile list"""
    # Get all profiles
    profiles = UserProfile.objects.all().order_by('-created_at')
    
    # Handle form submission
    if request.method == 'POST':
        form = UserProfileForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile created successfully!')
            return redirect('home')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = UserProfileForm()
    
    context = {
        'form': form,
        'profiles': profiles,
        'total_count': profiles.count(),
        'section': 'home',
    }
    return render(request, 'root/home.html', context)

def dashboard(request):
    """Main dashboard view with statistics"""
    # Statistics for dashboard
    total_profiles = UserProfile.objects.count()
    active_profiles = UserProfile.objects.filter(is_active=True).count()
    inactive_profiles = UserProfile.objects.filter(is_active=False).count()
    
    # Recent profiles (last 10)
    recent_profiles = UserProfile.objects.all()[:10]
    
    # Education distribution
    education_stats = UserProfile.objects.values('education').annotate(count=Count('education'))
    
    context = {
        'total_profiles': total_profiles,
        'active_profiles': active_profiles,
        'inactive_profiles': inactive_profiles,
        'recent_profiles': recent_profiles,
        'education_stats': education_stats,
        'section': 'dashboard',
    }
    return render(request, 'root/dashboard.html', context)

def profile_list(request):
    """List all user profiles with search and filter"""
    search_query = request.GET.get('search', '')
    profiles = UserProfile.objects.all()
    
    if search_query:
        profiles = profiles.filter(
            Q(name__icontains=search_query) | 
            Q(email__icontains=search_query) |
            Q(profession__icontains=search_query)
        )
    
    context = {
        'profiles': profiles,
        'search_query': search_query,
        'total_count': profiles.count(),
        'section': 'profiles',
    }
    return render(request, 'root/profile_list.html', context)

def profile_create(request):
    """Create a new user profile"""
    if request.method == 'POST':
        form = UserProfileForm(request.POST)
        if form.is_valid():
            form.save()  # Saves all fields using __all__
            messages.success(request, 'Profile created successfully!')
            return redirect('profile_list')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = UserProfileForm()
    
    context = {
        'form': form,
        'title': 'Create Profile',
        'section': 'profiles',
    }
    return render(request, 'root/profile_form.html', context)

def profile_update(request, pk):
    """Update an existing user profile"""
    profile = get_object_or_404(UserProfile, pk=pk)
    
    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()  # Updates profile using __all__
            messages.success(request, 'Profile updated successfully!')
            return redirect('profile_list')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = UserProfileForm(instance=profile)
    
    context = {
        'form': form,
        'profile': profile,
        'title': 'Update Profile',
        'section': 'profiles',
    }
    return render(request, 'root/profile_form.html', context)

def profile_delete(request, pk):
    """Delete a user profile"""
    profile = get_object_or_404(UserProfile, pk=pk)
    
    if request.method == 'POST':
        profile.delete()
        messages.success(request, 'Profile deleted successfully!')
        return redirect('profile_list')
    
    context = {
        'profile': profile,
        'section': 'profiles',
    }
    return render(request, 'root/profile_confirm_delete.html', context)

def profile_detail(request, pk):
    """View profile details"""
    profile = get_object_or_404(UserProfile, pk=pk)
    
    context = {
        'profile': profile,
        'section': 'profiles',
    }
    return render(request, 'root/profile_detail.html', context)
