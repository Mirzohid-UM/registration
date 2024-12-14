from django.http import JsonResponse
from .forms import UserProfileForm
from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.auth import login as auth_login
from .test import TestScoreForm, AdditionalDocument
from django.shortcuts import render
from .Profile import Userprofile
from django.contrib.auth.decorators import login_required
from PIL import Image
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import CustomUser
import logging
import yaml
from django.db import transaction

@receiver(post_save, sender=CustomUser)
def my_handler(sender, instance, created, **kwargs):
    if created:
        # Yangi foydalanuvchi yaratildi
        print(f"Yangi foydalanuvchi: {instance}")

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            # UserProfile'dan foydalanuvchini qidiramiz
            user_profile = CustomUser.objects.get(username=username)

            # Parolni tekshirish (hashlash ishlatilmagan bo'lsa)
            if user_profile.password == password:  # Bu joyda hash funksiyasi qo'llang
                auth_login(request, user_profile)  # Tizimga kirish
                return redirect('profile')  # Muvaffaqiyatli login
            else:
                messages.error(request, "Invalid password.")
        except CustomUser.DoesNotExist:
            messages.error(request, "User not found.")

    return render(request, 'HTML/login.html')
@login_required
def profile_view(request):
    user = request.user  # Bu AbstractUser asosida ishlatiladi
    profile, created = CustomUser.objects.get_or_create(username=request.user.username)
    user_scores = CustomUser.objects.filter(username=user.username)  # username orqali filtrlaymiz
    return render(request, 'HTML/profile.html', {'profile': profile, 'user_scores': user_scores})
@login_required
def profile_edit_view(request):
    try:
        # UserProfile modelidan foydalanish
        profile, created = CustomUser.objects.get_or_create(username=request.user.username)
    except CustomUser.DoesNotExist:
        profile = CustomUser(username=request.user.username)
        profile.save()

    # Formni ishlatish
    if request.method == "POST":
        form = Userprofile(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = Userprofile(instance=profile)

    return render(request, 'HTML/profile_edit.html', {'form': form})

def validate_form_data(request):
    if request.method == 'POST':
        form = UserProfileForm(request.POST)
        if form.is_valid():
            # Agar ma'lumot to‘g‘ri bo‘lsa, muvaffaqiyat xabarini yuboramiz
            return JsonResponse({'success': True, 'message': 'Form ma’lumotlari to‘g‘ri!'})
        else:
            # Xatoliklarni qaytarish
            errors = {field: error[0]['message'] for field, error in form.errors.get_json_data().items()}
            return JsonResponse({'success': False, 'errors': errors})


def succes_view(request):
    # Misol uchun oddiy ro'yxat ma'lumotlari
    items = ["Item 1", "Item 2", "Item 3"]
    return render(request, 'HTML/success.html', {'items': items})


def register(request):
    if request.method == 'POST':
        form = UserProfileForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Ro\'yxatdan o\'tdingiz!')
            return redirect('succes')
    else:
        form = UserProfileForm()

    return render(request, 'HTML/register.html', {'form': form})

logger = logging.getLogger(__name__)
from django.db import transaction

@login_required
def add_score_view(request):
    if request.method == 'POST':
        form = TestScoreForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                # Tranzaksiyaga qo'yish
                with transaction.atomic():
                    # Test score ni saqlash
                    test_score = form.save()

                    # Fayllarni saqlash
                    additional_docs = request.FILES.getlist('additional_documents', [])
                    for file in additional_docs:
                        AdditionalDocument.objects.create(test_score=test_score, file=file)

                    messages.success(request, 'Arizangiz muvaffaqiyatli yuborildi!')
                    return redirect('profile')  # Profilga qaytish

            except Exception as e:
                logger.error(f"Ma'lumotni saqlashda xatolik: {str(e)}")
                messages.error(request, "Ma'lumotni saqlashda xatolik yuz berdi. Iltimos, qayta urinib ko'ring.")
        else:
            logger.warning(f"Forma xatolari: {form.errors}")
            messages.error(request, 'Formada xatolar bor. Iltimos, maʼlumotlarni tekshiring.')
    else:
        form = TestScoreForm()

    return render(request, 'HTML/add_score.html', {'form': form})


@receiver(post_save, sender=CustomUser)
def resize_profile_picture(sender, instance, created, **kwargs):
    if instance.profile_picture:
        img = Image.open(instance.profile_picture)
        img = img.resize((150, 150))  # Rasmni 150x150 ga o'zgartirish
        img.save(instance.profile_picture.path)
def index(request):
    return render(request, 'HTML/index.html')
def team_view(request):
    return render(request, 'HTML/team.html')

# Testimonial sahifasi
def testimonial_view(request):
    return render(request, 'HTML/testimonial.html')

# Contact sahifasi
def contact_view(request):
    return render(request, 'HTML/contact.html')

# 404 sahifasi
def custom_404_view(request, exception=None):
    return render(request, 'HTML/404.html', status=404)
def render_static_files(request):
    # YAML faylini o'qish
    with open('static_files.yaml', 'r') as file:
        yaml_content = yaml.safe_load(file)

    # Static fayllarni HTML shabloniga yuborish
    return render(request, 'show_static_files.html', {'static_files': yaml_content['static_files']})