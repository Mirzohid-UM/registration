from django import forms
from .models import CustomUser


class UserProfileForm(forms.ModelForm):
    date_of_birth = forms.DateField(required=False, widget=forms.TextInput(attrs={'type': 'date'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'id': 'password'}))
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={'id': 'confirmPassword'}))
    help_text = "Parol 8 ta belgidan kam bo'lmasligi kerak."""
    class Meta:
        model = CustomUser
        fields = ['first_name', 'username','last_name', 'email', 'date_of_birth', 'phone_number', 'address', 'password']
    def clean_date_of_birth(self):
        date_of_birth = self.cleaned_data.get('date_of_birth')
        if not date_of_birth:
            raise forms.ValidationError("Tug'ilgan sana talab qilinadi.")
        return date_of_birth



    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password != confirm_password:
            self.add_error('confirm_password', "Passwords do not match.")
        return cleaned_data

    def clean_email(self):
        email = self.cleaned_data.get('email')
        allowed_domains = ["gmail.com", "yahoo.com"]  # Ruxsat etilgan domenlar
        email_domain = email.split('@')[-1]

        if email_domain not in allowed_domains:
            raise forms.ValidationError(
                f"Elektron pochta domeni faqat {', '.join(allowed_domains)} bo‘lishi kerak."
            )

        return email