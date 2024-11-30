# myapp/views.py
from django.shortcuts import render

def home(request):
    return render(request, '../index.html')

def who_we_are(request):
    return render(request, 'who_we_are.html')

def what_we_do(request):
    return render(request, 'what_we_do.html')

def institute(request):
    return render(request, 'institute.html')  # Make sure you have 'institute.html' template

def projects(request):
    return render(request, 'projects.html')

def contact(request):
    return render(request, 'contact.html')
