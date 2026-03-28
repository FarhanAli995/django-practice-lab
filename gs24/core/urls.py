from django.urls import path
from core import views


urlpatterns = [
    path('', views.showdata, name='showdata'),
    path('teacher/', views.show_teacher_data, name='show_teacher_data'),
    path('employee/', views.show_employee_data, name='show_employee_data'),
]
