from django import forms
from app.models import *

class StudentRegistrationForm(forms.ModelForm):
    class Meta:
        ## this is our model name here we are defining
        model = Student
        ## in fields what we want to display in FE here we defining
        fields = '__all__'
        widgets = {
            'student_name' : forms.TextInput(attrs={'class': 'form-control'}),
            'student_email' : forms.TextInput(attrs={'class': 'form-control'}),
            'student_gender' : forms.TextInput(attrs={'class': 'form-control'}),
            'student_address' : forms.TextInput(attrs={'class': 'form-control'}),
            'student_course' : forms.TextInput(attrs={'class': 'form-control'}),
        }
