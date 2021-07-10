from django import forms

from fscohort.models import Student

# class StudentForm(forms.Form):
#     first_name = forms.CharField(max_length=100, label="Your Name")
#     last_name = forms.CharField(max_length=100, label="Your Surname")
#     number = forms.IntegerField(required=False)

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ["first_name", "last_name", "number"]
