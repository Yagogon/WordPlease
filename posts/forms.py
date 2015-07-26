from django import forms
from material import Layout, Row, Fieldset, LayoutMixin
from posts.models import Post
import datetime


class PostForm(forms.ModelForm, Layout):

    class Meta:
        model = Post
        exclude = ['owner']
