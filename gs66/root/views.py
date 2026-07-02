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


def stu_sub_details(request, my_id, my_sub_id):
    # Convert my_sub_id to int because URLs capture it as a string by default
    try:
        student_id = int(my_sub_id)
    except ValueError:
        student_id = my_sub_id

    if my_id and student_id == 1:
        context = {"my_sub_id": my_sub_id, 
        "my_id": my_id, "name": "Farhan Ali", 
        "info":"First year",
        "subjects":["Maths","Physics"]}
    elif my_id and student_id == 2:
        context = {"my_sub_id": my_sub_id, 
        "my_id": my_id, "name": "Ahmed Ali",
        "info":"Second year",
        "subjects":["Chemistry","Biology"]}
    elif my_id and student_id == 3:
        context = {"my_sub_id": my_sub_id,
        "my_id": my_id, 
        "name": "Ali Hasan", 
        "info":"Third year",
        "subjects":["Computer Science","Programming"]}
    else:
        context = {"my_sub_id": my_sub_id, 
        "my_id": my_id, 
        "name": "No such student",
        "info":"No such info",
        "subjects":["No such subjects"]}
    
    # Pass the context (which contains my_id and name) to the template
    return render(request, 'root/sub_students.html', context)