from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from .models import Student


def index(request):
    students = Student.objects.all()
    #list_students = ", "\
    #   .join([student.name for student in students])
    #return HttpResponse(list_students)
    dictionary = {'students':students}
    return render(request,'udl/index.html',dictionary)