# profil/forms.py
from django import forms
from django.core.exceptions import ValidationError
from .models import Hero, About

class HeroForm(forms.ModelForm):
    class Meta:
        model = Hero
        fields = '__all__'

    def clean(self):
        cleaned_data = super().clean()
        if not self.instance.pk and Hero.objects.exists():
            raise ValidationError("Hanya boleh ada satu data Hero.")
        return cleaned_data
    
class AboutForm(forms.ModelForm):
    class Meta:
        model = About
        fields = '__all__'

    def clean(self):
        cleaned_data = super().clean()
        if not self.instance.pk and About.objects.exists():
            raise ValidationError("Hanya boleh ada satu data About.")
        return cleaned_data