from django import forms
from .models import RedgModel

class RedgForm(forms.ModelForm):
    class Meta:
        model = RedgModel
        fields = '__all__'