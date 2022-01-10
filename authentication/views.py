from django.urls import reverse_lazy
from .forms import RegisterForm
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView, PasswordResetView, \
    PasswordResetDoneView, PasswordResetConfirmView
from django.views.generic import CreateView


class CustomLoginView(LoginView):
    template_name = 'login.html'
    next_page = 'index'


class RegistrationView(CreateView):
    template_name = 'register.html'
    form_class = RegisterForm
    success_url = reverse_lazy('login')


class CustomPasswordChangeView(PasswordChangeView):
    template_name = 'change_pass.html'
    success_url = reverse_lazy('index')


class CustomPasswordResetView(PasswordResetView):
    template_name = 'forgotten_pass.html'
    success_url = reverse_lazy('done')


class CustomPasswordResetDoneView(PasswordResetDoneView):
    template_name = 'done.html'


class CustomPasswordResetConfirmView(PasswordResetConfirmView):
    template_name = 'reset.html'
    success_url = reverse_lazy('index')


class CustomLogoutView(LogoutView):
    next_page = 'index'

