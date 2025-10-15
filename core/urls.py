from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("about", views.about, name="about"),
    path("experience", views.experience, name="experience"),
    path("projects", views.projects, name="projects"),
    path("contact", views.contact, name="contact"),
]