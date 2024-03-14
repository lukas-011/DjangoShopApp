from .models import Course
from django.shortcuts import render

def index(request):
    courses = Course.objects.all()
    return render(request, 'courses.html', {'courses': courses})

def single_course(request, course_id):
    course = Course.object.get(pk=course_id)
    return render(request, 'single_course.html', {'course': course})
