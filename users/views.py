# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect
from django.contrib.auth import logout as django_logout, authenticate
from django.contrib.auth import login as django_login
from django.contrib.auth.models import User
from users.forms import LoginForm, SignupForm
from django.views.generic import View
from vanilla import CreateView
from django.core.urlresolvers import reverse_lazy

class LoginView(View):

    def get(self, request):

        error_messages = []

        form = LoginForm()

        context = {
            'errors': error_messages,
            'form': form
        }

        return render(request, 'users/login.html', context)


    def post(self, request):

        error_messages = []
        form = LoginForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data.get('usr')
            password = form.cleaned_data.get('pwd')
            user = authenticate(username=username, password=password)

            if user is None:
                error_messages.append('Nombre de usuario o contraseña incorrectos')
            else:
                if user.is_active:
                    django_login(request, user)
                    url = request.GET.get('next', 'posts_home')
                    return redirect(url)
                else:
                    error_messages.append('El usuario no esta activo')


        context = {
            'errors': error_messages,
            'login_form': form
        }

        return render(request, 'users/login.html', context)


class LogoutView(View):

    def get(self, request):

        if request.user.is_authenticated():
            django_logout(request)

        return redirect('posts_home')

class VanillaSignupView(CreateView):

    model = User
    success_url = reverse_lazy('posts_home')
    template_name = 'users/signup.html'

    def get_form(self, data=None, files=None, **kwargs):

        return SignupForm(data, files, **kwargs)

    def form_valid(self, form):

        form.save()
        username = form.cleaned_data.get('usr')
        password = form.cleaned_data.get('pwd')
        user = authenticate(username=username, password=password)
        return redirect(self.success_url)

class SignupView(View):

    def get(self, request):

        error_messages = []
        form = SignupForm()

        context = {

            'errors': error_messages,
            'form' : form

        }

        return render(request, 'users/signup.html', context)

    def post(self, request):

        form = SignupForm(request.POST)

        if form.is_valid():
            new_user = form.save()
            user = authenticate(username=new_user.username, password=new_user.password)
            if user is not None:
                django_login(request, user)
                url = request.GET.get('next', 'posts_home')
                return redirect(url)

        error_messages = []
        context = {
            'errors': error_messages,
            'login_form': form
        }

        return render(request, 'posts/signup.html', context)





