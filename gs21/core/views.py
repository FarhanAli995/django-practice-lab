from django.shortcuts import render

# Create your views here.
def function(request):
    template_name = 'template.html'
    context = {}

    if request.method == 'GET':
        pass

    if request.method == 'POST':
        pass

    return render(request, template_name, context)
