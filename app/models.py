from django.contrib.auth.models import User
from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)  # User modeliga bog'lash
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)  # Email qo'shish
    username = models.CharField(max_length=100, unique=True)  # Username qo'shish
    date_of_birth = models.DateField()
    phone_number = models.CharField(max_length=20)
    address = models.TextField()

    def __str__(self):
        return self.user.username



