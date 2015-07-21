from django import forms
from django.contrib.auth.models import User
from material import Layout, Row, Fieldset, LayoutMixin

class LoginForm(forms.ModelForm, Layout):

    class Meta:
        model = User
        fields = ['username', 'password']

class SignupForm(forms.ModelForm, Layout):


    class Meta:
        model = User
        fields = ['first_name','last_name', 'username', 'password']

