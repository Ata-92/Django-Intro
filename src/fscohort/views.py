from django.shortcuts import render
from django.http import HttpResponse
from fscohort.forms import StudentForm

from fscohort.models import Student

# Create your views here.
def index(request):
    return render(request, 'fscohort/home.html')

def student_num(request):
    students = Student.objects.all()
    num_of_stdnt = Student.objects.count()
    context = {
        "students": students,
        "num": num_of_stdnt
    }
    return render(request, 'fscohort/student_list.html', context)

def student_add(request):
    form = StudentForm()
    context = {
        'form': form
    }
    return render(request, 'fscohort/student_add.html', context)
