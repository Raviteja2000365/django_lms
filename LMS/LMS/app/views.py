from django.shortcuts import render
from .models import Courses,assignments,announcements,quiz


def courses(request):
    courses = Courses.objects.all()
    return render(request, "courses.html", {"courses": courses})  # Pass the fetched objects to the template

def Assaigment(request):
    assignment = assignments.objects.all().order_by('-date')  # Fetch all course objects
    return render(request, "assignments.html", {"assignments": assignment})  # Pass the fetched objects to the template

def Announcements(request):
    Announcements = Courses.objects.all().order_by('-date')  # Fetch all course objects
    return render(request, "announcements.html", {"Announcements": Announcements})  # Pass the fetched objects to the template




# Create your views here.
def MAIN(request):
    return render(request,"lms.html")