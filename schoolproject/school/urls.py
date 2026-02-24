
from django.urls import path
from school import views


urlpatterns = [
    path('', views.learn_django, name='learn_django'),
    path('qwe/', views.django, name='django'),
    path('python/', views.learn_python, name='learn_python'),
    path('bestCourse/',views.best_course, name='best_course'),
]