from .models import Meme
from django import forms
from .models import Comment

class CommentRegisterForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ['content']
        