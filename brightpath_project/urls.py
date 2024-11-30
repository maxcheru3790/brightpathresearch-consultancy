# brightpath_project/urls.py
from django.contrib import admin
from django.urls import path, include  # Import 'include' for including app URLs

urlpatterns = [
    path('admin/', admin.site.urls),  # Django Admin interface URL
    path('', include('myapp.urls')),  # Include the URL configuration from 'myapp'
]
