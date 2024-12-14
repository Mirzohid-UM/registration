"""
URL configuration for login project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# login/urls.py
# urls.py
from django.urls import path
from app import views
# views.py-dan import qilish
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin

urlpatterns = [
    path('', views.succes_view, name='succes'),
    path('validate-form/', views.validate_form_data, name='validate_form'),
    path('profile/', views.profile_view, name='profile'),
    path('index/', views.index, name='index'),
    path('succes/', views.succes_view, name='succes'),
    path('login/', views.login_view, name='login'),  # Login sahifasi
    path('register/', views.register, name='register'),
    path('add_score/', views.add_score_view, name='add_score'),  # Register sahifasi
    path('profile/edit/', views.profile_edit_view, name='profile_edit'),
    path('custom_404_view', views.custom_404_view, name='custom_404' ),
    path('contact_view', views.contact_view, name='contact_view'),
    path('testimonial_view',views.testimonial_view, name='testimonial_view'),
    path('team_view',views.team_view, name='team_view'),
    path('admin/', admin.site.urls),


]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

