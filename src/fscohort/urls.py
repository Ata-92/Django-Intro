from django.urls import path
from .views import index, student_num, student_add

urlpatterns = [
    path("", index, name="index"),
    path('num/', student_num, name='student_num'),
    path('add/', student_add, name='student_add'),
]
