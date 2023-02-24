from django import forms
from .models import image

class imageform(forms.ModelForm):
    class meta:
        model=image
        fields='__all__'