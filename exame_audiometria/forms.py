from django import forms
from .models import ExameAudiometria


class ExameAudiometriaForm(forms.ModelForm):
    class Meta:
        model = ExameAudiometria
        fields = '__all__'