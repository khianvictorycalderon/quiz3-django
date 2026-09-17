from django import forms

from .models import Student


class StudentForm(forms.ModelForm):

    class Meta:
        model = Student

        fields = [
            "first_name",
            "last_name",
            "course",
        ]

        widgets = {
            "first_name": forms.TextInput(attrs={
                "class": (
                    "w-full px-4 py-2.5 rounded-xl "
                    "bg-neutral-900 border border-neutral-700 "
                    "text-neutral-100 placeholder-neutral-500 "
                    "outline-none transition "
                    "focus:border-indigo-500 focus:ring-2 "
                    "focus:ring-indigo-500/20"
                ),
                "placeholder": "Juan",
            }),

            "last_name": forms.TextInput(attrs={
                "class": (
                    "w-full px-4 py-2.5 rounded-xl "
                    "bg-neutral-900 border border-neutral-700 "
                    "text-neutral-100 placeholder-neutral-500 "
                    "outline-none transition "
                    "focus:border-indigo-500 focus:ring-2 "
                    "focus:ring-indigo-500/20"
                ),
                "placeholder": "Dela Cruz",
            }),

            "course": forms.TextInput(attrs={
                "class": (
                    "w-full px-4 py-2.5 rounded-xl "
                    "bg-neutral-900 border border-neutral-700 "
                    "text-neutral-100 placeholder-neutral-500 "
                    "outline-none transition "
                    "focus:border-indigo-500 focus:ring-2 "
                    "focus:ring-indigo-500/20"
                ),
                "placeholder": "BSIT",
            }),
        }