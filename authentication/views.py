from django.contrib.auth import logout, authenticate,login
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm, \
    PasswordResetForm, PasswordChangeForm, SetPasswordForm, UserCreationForm


def logIN(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request,username=username,password=password)
        if user:
            login(request,user)
            return redirect('index')

    form = AuthenticationForm()

    context = {
        'form': form
    }
    return render(request, 'login.html', context)


def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(request, username=username, password=password)
            login(request, user)
            return redirect('index')
    else:
        form = UserCreationForm()

    context = {
        'form': form
    }
    return render(request, 'register.html', context)


def log_out(request):
    logout(request)
    return redirect('index')
