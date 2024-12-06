from django.contrib import admin
from .models import TestScore


@admin.register(TestScore)
class TestScoreAdmin(admin.ModelAdmin):
    list_display = ('user', 'school_name', 'is_studying', 'study_level', 'current_activity')
    search_fields = ('school_name', 'user__username')  # Foydalanuvchi username va maktab nomi bo'yicha qidirish
    list_filter = ('study_level', 'is_studying')  # Filtrlar
    ordering = ('-user',)  # Tartib
