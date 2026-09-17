from django.shortcuts import get_object_or_404, redirect, render

from .forms import StudentForm
from .models import Student


def retrieve_student_records(request):
    records = Student.objects.all().order_by("id")

    return render(request, "main/home.html", {
        "all_records": records,
        "form": StudentForm(),
    })


def add_student(request):
    if request.method == "POST":
        form = StudentForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("home")

    return render(request, "main/home.html", {
        "all_records": Student.objects.all().order_by("id"),
        "form": form,
    })


def delete_student(request, student_id):
    if request.method == "POST":
        student = get_object_or_404(Student, id=student_id)
        student.delete()

    return redirect("home")