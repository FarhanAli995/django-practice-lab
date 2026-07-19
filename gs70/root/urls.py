from django.urls import path
from . import views

app_name = 'root'

urlpatterns = [
    path('', views.StudentFormView.as_view(), name='student_form'),
    path('teacher/', views.TeacherFormView.as_view(), name='teacher_form'),
    path('student-success/', views.student_success_page, name='student_success'),
    path('teacher-success/', views.teacher_success_page, name='teacher_success'),
]
