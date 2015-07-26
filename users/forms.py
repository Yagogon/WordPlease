from django import forms
from django.contrib.auth.models import User
from material import Layout, Row, Fieldset, LayoutMixin

class LoginForm(forms.Form, Layout):

    usr = forms.CharField(label="Nombre de usuario")
    pwd = forms.CharField(label="Password", widget=forms.PasswordInput())

class SignupForm(forms.ModelForm, Layout):

    password = forms.CharField(label="Password", widget=forms.PasswordInput())
    class Meta:
        model = User
        fields = ['first_name','last_name', 'email','username']

