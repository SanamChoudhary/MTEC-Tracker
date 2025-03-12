from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import studentInformationModel, dateOfCleanup
from .forms import studentFormSet, cleanUpDateForm, studentInformationForm

# Create your views here.

def home(request):
    return render(request, "home.html")

def create(request):
    if request.method == "POST":
        cleanupForm = cleanUpDateForm(request.POST)
        studentForm = studentFormSet(request.POST)

        if cleanupForm.is_valid() and studentForm.is_valid():
            cleanup = cleanupForm.save()
            students = studentForm.save(commit=False)
            for student in students:
                student.cleanup = cleanup
                student.save()
            # Reinitialize studentFormSet to be empty
            studentForm = studentFormSet()

        return render(request, "create.html", {
            "cleanupForm": cleanupForm,
            "studentFormSet": studentForm
        })

    else:
        cleanupForm = cleanUpDateForm()
        studentForm = studentFormSet()

    return render(request, "create.html", {
        "cleanupForm": cleanupForm,
        "studentFormSet": studentForm
    })

def view(request):
    cleanups = dateOfCleanup.objects.all().order_by('date')
    cleanup_data = []
    for cleanup in cleanups:
        students = studentInformationModel.objects.filter(cleanup=cleanup)
        cleanup_data.append({
            'cleanup': cleanup,
            'students': students
        })
    return render(request, "view.html", {"cleanup_data": cleanup_data})

def functions(request):
    cleanups = dateOfCleanup.objects.all().order_by('date')
    cleanup_dates = []
    student_counts = []

    for cleanup in cleanups:
        students = studentInformationModel.objects.filter(cleanup=cleanup)
        cleanup_dates.append(cleanup.date)
        student_counts.append(students.count())

    return render(request, "functions.html", {
        "cleanup_dates": cleanup_dates,
        "student_counts": student_counts
    })