from django.urls import path, register_converter
from . import views, converters

register_converter(converters.Four_digit_year_converter, "yyyy")

urlpatterns = [
    path('session/<yyyy:year>/',views.home, name= "details")
]
