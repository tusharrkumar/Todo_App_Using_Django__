from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from app.forms import *

from app.models import *
## Create your views here.



## this function will add new item and displaying the items
## here data has been saved in database
def add_show(request):
    if request.method == 'POST':
        stu_form_obj = StudentRegistrationForm(request.POST)
        if stu_form_obj.is_valid():
            ## when we have to validate multiple field or we have more than one field we use cleaned_data
            name = stu_form_obj.cleaned_data['student_name']
            gender = stu_form_obj.cleaned_data['student_gender']
            address = stu_form_obj.cleaned_data['student_address']
            course = stu_form_obj.cleaned_data['student_course']
            register = Student(student_name=name, student_gender=gender, student_address=address, student_course=course)
            register.save()
            stu_form_obj = StudentRegistrationForm()
            
            # if stu_form_obj == register:
                # stu_form_obj = StudentRegistrationForm()
                # return HttpResponse("<script>alert('Student Already Exist')</script>")

                # register.save()
                # stu_form_obj = StudentRegistrationForm()
                # return HttpResponse("<script>alert('Student Added Successfully')</script>")
    else:
        stu_form_obj = StudentRegistrationForm()
    stud = Student.objects.all()    ## --> retrieving data 
    d = { 'stu_form_obj':stu_form_obj, 'stu':stud }
    return render(request, 'add_show.html',d)



## this function will Update/Edit
def update_data(request, id):
    if request.method == 'POST':
        pi = Student.objects.get(pk=id)
        stu_obj_with_data = StudentRegistrationForm(request.POST, instance=pi)
        if stu_obj_with_data.is_valid():
            stu_obj_with_data.save()
            return HttpResponseRedirect(reverse('add_show'))
    else:
        pi = Student.objects.get(pk=id)
    stu_obj = StudentRegistrationForm(instance=pi)
    d = { 'form':stu_obj }
    return render(request, 'update_student.html',d)





## this function will delete
def delete_data(request, id):   #$ --> we have to create dynamic view
    if request.method == 'POST':
        delete_stu_obj = Student.objects.get(pk=id)
        delete_stu_obj.delete()
        return HttpResponseRedirect(reverse('add_show'))    ## --> in reverse() we have to give the exact view name where we want to go after deteting the data