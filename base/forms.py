from django import forms
from django.core.exceptions import ValidationError
from django.forms import ModelForm, Form
from base.models import Position


class TempForm(Form):
    title = forms.CharField(max_length=100)

    def clean_title(self, *args, **kwargs):
        raise ValidationError('Oops')