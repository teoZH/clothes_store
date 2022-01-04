from django.forms import ModelForm
from django.contrib.auth.forms import AuthenticationForm, \
    PasswordResetForm, PasswordChangeForm, SetPasswordForm, UserCreationForm, UsernameField
from .models import UserProfile


class RegisterForm(UserCreationForm):
    class Meta:
        model = UserProfile
        fields = ("username", 'image')
        field_classes = {'username': UsernameField}
