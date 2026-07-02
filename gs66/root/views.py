from django.shortcuts import render
# Create your views here.

def home_view(request):
    # Pass a list of student IDs to the template
    student_ids = range(1, 100) # You can change this to any list or database query
    return render(request, 'root/home.html', {'students': student_ids})

# def stu_details(request, my_id):
#     my_id = {'my_id':my_id}
#     return render(request, 'root/students.html',my_id) 


def stu_details(request, my_id):
    # Convert my_id to int because URLs capture it as a string by default
    try:
        student_id = int(my_id)
    except ValueError:
        student_id = my_id

    if student_id == 1:
        context = {"my_id": my_id, "name": "Farhan Ali"}
    elif student_id == 2:
        context = {"my_id": my_id, "name": "Ahmed Ali"}
    elif student_id == 3:
        context = {"my_id": my_id, "name": "Ali Hasan"}
    else:
        context = {"my_id": my_id, "name": "No such student"}
    
    # Pass the context (which contains my_id and name) to the template
    return render(request, 'root/students.html', context)