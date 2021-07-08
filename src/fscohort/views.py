from django.shortcuts import render
from django.http import HttpResponse

from fscohort.models import Student

# Create your views here.
def index(request):
    return HttpResponse("<h1>Hello world!</h1>")

def student_num(request):
    num_of_stdnt = Student.objects.count()
    return HttpResponse("FS Cohort has {} students". format(num_of_stdnt))
