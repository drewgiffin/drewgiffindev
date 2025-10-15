from django.shortcuts import render

from .forms import ContactForm

def index(request):
    return render(request, "home.html")

def about(request):
    return render(request, "about.html")

def experience(request):
    return render(request, "experience.html")

def projects(request):
    return render(request, "projects.html")

def contact(request):
    if request.method == "POST":
        return render(request, "contact.html")
    else:
        form = ContactForm()
        return render(request, "contact.html", {"form": form})