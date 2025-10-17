from django import template
from pathlib import Path

register = template.Library()

@register.filter
def clean_base_name(value):
    path = Path(value)
    file_name = path.stem.replace("_", " ")
    return file_name

@register.filter
def create_range(value):
    return range(value)
