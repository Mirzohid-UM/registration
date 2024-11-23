from django import forms
from django.core.exceptions import ValidationError
from .models import User
from .models import UserProfile


class UserProfileForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={'id': 'password'}))
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={'id': 'confirmPassword'}))
    help_text = "Parol 8 ta belgidan kam bo'lmasligi kerak."
    date_of_birth = forms.DateField(required=True, widget=forms.TextInput(attrs={'type': 'date'}))

    class Meta:
        model = UserProfile
        fields = ['first_name', 'last_name', 'date_of_birth', 'phone_number', 'username', 'address', 'email']

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError('Ushbu username allaqachon mavjud.')
        return username


    def clean_email(self):

        email = self.cleaned_data.get('email')
        allowed_domains = ['example.com', 'gmail.com', 'yahoo.com']  # Ruxsat etilgan domenlar ro‘yxati
        domain = email.split('@')[-1]  # Domenni olish

        if domain not in allowed_domains:
            raise ValidationError('Email ruxsat etilgan domenlardan bo‘lishi kerak!')
        return email

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password != confirm_password:
            self.add_error('confirm_password', "Passwords do not match.")

        return cleaned_data
