from django.forms import ModelForm
from .models import UserAvatar


class UserAvatarForm(ModelForm):
    class Meta:
        model = UserAvatar
        fields = ['image']