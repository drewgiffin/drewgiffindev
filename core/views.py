from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, "home.html")

def about(request):
    return render(request, "about.html")

def experience(request):
    return render(request, "experience.html")

def contact(request):
    return render(request, "contact.html")