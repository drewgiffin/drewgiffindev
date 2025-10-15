from django import forms
from django.core.validators import RegexValidator

class ContactForm(forms.Form):
    name = forms.CharField(label="Name", max_length=100)
    subject = forms.CharField(label="Subject", max_length=100)
    email = forms.EmailField(label="Email", max_length=100, required=False)
    message = forms.CharField(label="Message", max_length=1000, widget=forms.Textarea)