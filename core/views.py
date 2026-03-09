from django.shortcuts import render
from .forms import ContactForm
from django.core.mail import send_mail
from django.conf import settings

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
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data["subject"]
            message = form.cleaned_data["message"]
            email = form.cleaned_data["email"]
            send_mail(
                subject,
                f"Email: {email}\nMessage: {message}",
                settings.EMAIL_HOST_USER,
                ["drewgiffin@outlook.com"],
                fail_silently=False,
            )
        return render(request, "contact.html")
    else:
        form = ContactForm()
        return render(request, "contact.html", {"form": form})
