from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Field

from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.core.exceptions import ValidationError
from django.forms import ModelForm, Form


from base.models import Position, Employer


class TempForm(Form):
    title = forms.CharField(max_length=100)

    def clean_title(self, *args, **kwargs):
        raise ValidationError('Oops')




class EmployerCreationForm(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    password_confirm = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
        model = Employer
        fields = ('email', 'username')

    def clean_password_confirm(self):
        password = self.cleaned_data.get('password')
        password_confirm = self.cleaned_data.get('password_confirm')

        if password and password_confirm and password != password_confirm:
            raise ValidationError("Passwords don't match")
        return password_confirm



    def save(self, commit=True):
        user = super(EmployerCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data['password'])
        user.is_staff = True
        if commit:
            user.save()
        return user


class EmployerUpdateForm(forms.ModelForm):
    class Meta:
        model = Employer
        fields = ('first_name', 'last_name', 'email')


    def __init__(self, *args, ** kwargs):
        super(EmployerUpdateForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()

        self.helper.layout = Layout(
            Field('first_name'),
            Field('last_name'),
            Field('email'),
            Submit('submit', 'Update')
        )

    def clean_password(self):
        return self.initial['password']


