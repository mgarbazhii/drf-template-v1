from django.contrib.auth import views as auth_views
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path(r'auth/', include('djoser.urls')),
]

admin.site.site_header = "Панель администратора"
admin.site.index_title = "САЙТ"
