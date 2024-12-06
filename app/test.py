from django import forms
from .models import TestScore, AdditionalDocument
from django.db import models

class ApplicationForm(forms.Form):
    study_level = forms.ChoiceField(choices=[("Oliy ta'lim", "Oliy ta'lim"), ("O'rta ta'lim", "O'rta ta'lim")], required=True)
    university = forms.CharField(required=False)
    course_year = forms.CharField(required=False)
    school_name = forms.CharField(required=False)

    def clean(self):
        cleaned_data = super().clean()
        study_level = cleaned_data.get("study_level")

        if study_level == "Oliy ta'lim":
            if not cleaned_data.get("university"):
                self.add_error("university", "Universitet nomini kiriting.")
            if not cleaned_data.get("course_year"):
                self.add_error("course_year", "Kurs yili kiritilishi kerak.")
        elif study_level == "O'rta ta'lim":
            if not cleaned_data.get("school_name"):
                self.add_error("school_name", "Maktab nomi kiriting.")
        return cleaned_data


class TestScoreForm(forms.ModelForm):
    class Meta:
        model = TestScore
        fields = [
            'user',
            'citizenship',
            'school_name',
            'is_studying',
            'current_study',
            'course_year',
            'study_level',
            'current_activity',
            'achievements',
            'languages',
            'international_tests',
            # Fayllarni qo'shish
        ]
        widgets = {
            'achievements': forms.Textarea(attrs={'rows': 3}),
              # Fayllar uchun widget
        }

