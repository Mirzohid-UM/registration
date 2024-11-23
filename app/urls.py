from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('app.urls')),  # App ichidagi urls.py-ni import qilish
]
