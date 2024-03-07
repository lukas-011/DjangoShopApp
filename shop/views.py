from django.shortcuts import render
from django.http import HttpResponse
from .models import Course
from django.shortcuts import render

def index(request):
    courses = Course.objects.all()
    return render(request, 'courses.html', {'courses': courses})
