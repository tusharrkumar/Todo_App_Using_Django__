from django.contrib import admin
from app.models import *
## Register your models here.

@admin.register(Student)
class Student(admin.ModelAdmin):
    list_display = ('student_name', 'student_gender', 'student_address', 'student_course')


# admin.site.register(Student)