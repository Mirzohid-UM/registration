from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    date_of_birth = models.DateField(null=True, blank=True)
    phone_number = models.CharField(max_length=15, null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    bio = models.TextField(blank=True, null=True)
    profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.username


class TestScore(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, blank=True, null=True)
    citizenship = models.CharField(max_length=100, default='Uzbekistan')
    school_name = models.CharField(max_length=255,blank=True, null=True)
    is_studying = models.CharField(max_length=3,blank=True, choices=[('Yes', 'Ha'), ('No', 'Yo\'q')] )
    current_study = models.CharField(max_length=50, blank=True, null=True)
    course_year = models.CharField(max_length=50, default='1')  # Default qiymat qo'shildi
    study_level = models.CharField(
        max_length=50,blank=True,
        choices=[('Bachelor', 'Bakalavr'), ('Master', 'Magistr'), ('PhD', 'PhD'),]
    )
    current_activity = models.CharField(max_length=255 , blank=True, null=True)
    achievements = models.TextField(blank=True, null=True)
    languages = models.CharField(max_length=255, blank=True, null=True)
    international_tests = models.CharField(max_length=255, blank=True, null=True)


    def __str__(self):
        return f'{self.test_name} - {self.score}'


class AdditionalDocument(models.Model):
    test_score = models.ForeignKey(TestScore, on_delete=models.CASCADE, related_name='documents')
    file = models.FileField(upload_to='documents/')


