from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def fees_dj(request):
    return render(request, 'fees/feestwo.html', {
        'nm': 'django', 
        'st': '5',
        'p1': 56.24321,
        'p2': 56.00000,
        'p3': 56.36000

    })

def fees_py(request):
    stu = {'names': [
        'rahul',
        'sonam',
        'raj', 
        'anu'
    ]}
    return render(request, 'fees/feesone.html',stu)



def fees_3(request):
    stu ={'stu1' : {'name': 'Alice', 'fee': 1000},
    'stu2' : {'name': 'Bob', 'fee': 2000},
    'stu3': {'name': 'Charlie', 'fee': 3000},
    'stu4' : {'name': 'David', 'fee': 4000}
    }
    
    # Combine them into a list as discussed before
    all_students = {'stu5':stu}
    
    # 2. IMPORTANT: This return must be indented 4 spaces (inside the def)
    return render(request, 'fees/feesthree.html', all_students)
   
def fees_4(request):
    data={
        'stu1':{'name': 'farhan', 'roll':3343},
        'stu2':{'name': 'aly', 'roll':334},
        'stu3':{'name': 'far', 'roll':343},
        'stu4':{'name': 'faizan', 'roll':23343},
        'stu5':{'name': 'zoha', 'roll':33343},
        'stu6':{'name': 'zain', 'roll':33543},
        'stu7':{'name': 'zahid', 'roll':33543},
    }
    st={'data':data}
    return render(request, 'fees/fees_4.html', st)