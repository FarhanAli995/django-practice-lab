from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import AdmissionApplicationForm
from .models import AdmissionApplication

def admission_application(request):
    if request.method == 'POST':
        form = AdmissionApplicationForm(request.POST, request.FILES)
        if form.is_valid():
            # Process the cleaned data
            cleaned_data = form.cleaned_data

            # Save to database
            AdmissionApplication.objects.create(**cleaned_data)

            messages.success(request, 'Application submitted successfully!')
            return redirect('admission_success')
    else:
        form = AdmissionApplicationForm()

    return render(request, 'core/admission_form.html', {'form': form})

def success(request):
    return render(request, 'core/success.html') 