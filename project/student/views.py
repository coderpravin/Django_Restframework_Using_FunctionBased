from django.shortcuts import render,HttpResponse
from student.models import Student
from django.http import JsonResponse
# Create your views here.

def studentView(request):
    student = Student.objects.all().values()
    studentJson = list(student)
    return JsonResponse(studentJson, safe=False)