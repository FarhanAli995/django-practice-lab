from django.shortcuts import render, redirect, get_object_or_404
from .models import User
from .forms import UserForm

# Create your views here.

def home(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = UserForm()
    
    users = User.objects.all()
    context = {
        'form': form,
        'users': users,
    }
    return render(request, "root/home.html", context)


def edit_user(request, id):
    user = get_object_or_404(User, pk=id)
    if request.method == 'POST':
        form = UserForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = UserForm(instance=user)

    users = User.objects.all()
    context = {
        'form': form,
        'users': users,
        'edit_id': user.id,
    }
    return render(request, "root/home.html", context)


def delete_user(request, id):
    user = get_object_or_404(User, pk=id)
    if request.method == 'POST':
        user.delete()
    return redirect('home')