from django import forms
from .models import TestScore, AdditionalDocument
from django.db import models

class AdditionalDocumentForm(forms.ModelForm):
    class Meta:
        model = AdditionalDocument
        fields = ['file']
        widgets = {
            'file': forms.ClearableFileInput(attrs={'multiple': True}),
        }
