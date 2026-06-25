from django.shortcuts import render, redirect # Make sure redirect is imported!
from .forms import AdmissionApplicationForm

def admission_application(request):
    if request.method == "POST":
        form = AdmissionApplicationForm(request.POST)
        if form.is_valid():
            form.save()
            # redirect() tells Django to look at urls.py for the name="admission_success"
            return redirect('admission_success') 
            
    else:
        form = AdmissionApplicationForm()
        
    return render(request, "root/admission_form.html", {"form": form})

# Add this missing function that your urls.py is looking for!
def success(request):
    return render(request, "root/success.html")