from django.forms import ModelForm
from .models import Clothes


class ClothesForm(ModelForm):
    class Meta:
        model = Clothes
        fields = ['cloth_type', 'description', 'price', 'image']
