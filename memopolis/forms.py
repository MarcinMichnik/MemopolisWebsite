from .models import Meme
from django import forms

class MemeUpdateForm(forms.ModelForm):

    
    class Meta:
        model = Meme
        fields = []