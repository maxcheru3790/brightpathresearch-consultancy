# myapp/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='my_index'),  # Home page
    path('who-we-are/', views.who_we_are, name='who_we_are'),
    path('what-we-do/', views.what_we_do, name='what_we_do'),
    path('institute/', views.institute, name='institute'),  # Ensure this path matches
    path('projects/', views.projects, name='projects'),
    path('contact/', views.contact, name='contact'),
]
