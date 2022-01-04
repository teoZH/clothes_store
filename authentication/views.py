from django.contrib.auth import logout, authenticate, login
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm, \
    PasswordResetForm, PasswordChangeForm, SetPasswordForm, UserCreationForm

from .forms import RegisterForm
from django.http import HttpResponse
from django.http import Http404
from django.utils.encoding import force_str
from django.utils.http import urlsafe_base64_decode
from django.contrib.auth.tokens import default_token_generator
from django.db import transaction


def logIN(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('index')

    form = AuthenticationForm()

    context = {
        'form': form
    }
    return render(request, 'login.html', context)


def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(request, username=username, password=password)
            login(request, user)
            return redirect('index')
    else:
        form = RegisterForm()

    context = {
        'form': form
    }
    return render(request, 'register.html', context)


def change_password(request):
    form = PasswordChangeForm(user=request.user)
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')

    context = {
        'form': form
    }
    return render(request, 'change_pass.html', context=context)


def forgotten(request):
    form = PasswordResetForm()
    if request.method == 'POST':
        form = PasswordResetForm(request.POST)
        if form.is_valid():
            form.save(domain_override='http://127.0.0.1:8000')
            return redirect('done')

    context = {
        'form': form
    }
    return render(request, 'forgotten_pass.html', context)


def password_reset_confirm(request, uidb64, token):
    token_generator = default_token_generator
    user_id = force_str(urlsafe_base64_decode(uidb64))
    try:
        user = User.objects.get(pk=user_id)
        if not token_generator.check_token(user, token):
            return HttpResponse('WRONG!!!!!!!!!!!!!!!!')
    except (TypeError, ValueError, OverflowError, User.DoesNotExis):
        raise Http404()

    form = SetPasswordForm(user)
    if request.method == 'POST':
        form = SetPasswordForm(user, request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')

    context = {
        'form': form
    }
    return render(request, 'reset.html', context=context)


def done(request):
    return render(request, 'done.html')


def log_out(request):
    logout(request)
    return redirect('index')
