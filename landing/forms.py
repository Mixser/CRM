from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field, Submit
from django import forms
from django.contrib.auth import authenticate


class SignInForm(forms.Form):
    username = forms.CharField(label='Username', widget=forms.TextInput(attrs={'placeholder': 'Username'}))
    password = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))

    def __init__(self, *args, **kwargs):
        super(SignInForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()

        self.helper.form_class = 'form-signin'
        self.helper.label_class = 'col-lg-2'
        self.helper.field_class = 'form-control'

        self.helper.form_show_labels = False


        self.user = None

        self.helper.layout = Layout(
            Field('username', css_class='form-control'),
            Field('password', css_class='form-control'),
            Submit('submit', 'Signin', css_class='btn-lg btn-block')
        )

    def clean(self):
        cleaned_data = super(SignInForm, self).clean()
        username = cleaned_data['username']
        password = cleaned_data['password']
        user = authenticate(username=username, password=password)
        if user and user.is_active:
            self.user = user
            return cleaned_data

        msg = 'Please enter the correct username and password.'

        self.add_error('username', msg)
        self.add_error('password', msg)
