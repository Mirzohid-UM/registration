from django import forms
from .models import CustomUser  # Profile modeli nomini mos ravishda almashtiring

class Userprofile(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['bio', 'profile_picture', 'phone_number', 'address','date_of_birth', 'first_name', 'last_name']  # Maydonlarni aniqlang
        widgets = {
            'bio': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Write something about yourself...',
                'rows': 4,
            }),
            'profile_picture': forms.FileInput(attrs={
                'class': 'form-control',
            }),
            'phone_number': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter your phone number',
            }),
            'address': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter your address',
            }),
            'first_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter your first name',
            }),
            'last_name':forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter your last name',
            }),
            'date_of_birth': forms.DateInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter your date of birth',
                'type':'date',

            }),

        }
