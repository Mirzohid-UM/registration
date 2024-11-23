from django.contrib.auth import  login as auth_login
from django.contrib.auth.forms import AuthenticationForm
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from django.db import IntegrityError
from .forms import UserProfileForm
from .models import UserProfile
from django.contrib.auth.models import User
from django.db import transaction


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            return redirect('success')  # Login bo'lgandan so'ng bosh sahifaga yo'naltirish
        else:
            messages.error(request, 'Invalid username or password.', extra_tags='login')


    else:
        form = AuthenticationForm()

    return render(request, 'HTML/login.html', {'form': form})



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




def register(request):
    if request.method == 'POST':
        form = UserProfileForm(request.POST)
        if form.is_valid():
            user_data = form.cleaned_data
            try:
                with (transaction.atomic()):
                    user = User.objects.create_user(
                        username=user_data['username'],
                        email=user_data['email'],
                        password=user_data['password']
                    )
                    user_profile = UserProfile(
                        user=user,
                        first_name=user_data['first_name'],
                        last_name=user_data['last_name'],
                        date_of_birth=user_data['date_of_birth'],
                        phone_number=user_data['phone_number'],
                        address=user_data['address']
                    )
                    user_profile.save()
                    messages.success(request, 'Ro\'yxatdan o\'tdingiz!')
                    return redirect('login')
            except IntegrityError as e:
                    print(f"Xatolik: {e}")
                    if User.objects.filter(username=user_data['username']).exists():
                        form.add_error('username', 'Ushbu username allaqachon mavjud.')
                    if User.objects.filter(email=user_data['email']).exists():
                        form.add_error('email', 'Ushbu email allaqachon mavjud.')


    else:
        form = UserProfileForm()

    return render(request, 'HTML/register.html', {'form': form})

