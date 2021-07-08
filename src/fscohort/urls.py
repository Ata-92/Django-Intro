from django.urls import path
from .views import index, student_num

urlpatterns = [
    path("", index, name="index"),
    path('num/', student_num, name='student_num'),
]
