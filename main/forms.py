from django import forms
from django.core import validators
from django.core.validators import EmailValidator, RegexValidator
from django.core.exceptions import ValidationError
from .models import New


class PostForm(forms.ModelForm):
    class Meta:
        model = New
        fields = ['subject_uz', 'subject_ru', 'content_uz', 'content_ru', 'image']
