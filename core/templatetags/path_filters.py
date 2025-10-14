from django import template
from pathlib import Path

register = template.Library()

def clean_base_name(value):
    path = Path(value)
    file_name = path.stem.replace("_", " ")
    return file_name

register.filter("clean_base_name", clean_base_name)