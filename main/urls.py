from django.urls import path

from . import views

urlpatterns = [
    path("", views.retrieve_student_records, name="home"),
    path("add/", views.add_student, name="add_student"),
    path("delete/<int:student_id>/", views.delete_student, name="delete_student"),
]