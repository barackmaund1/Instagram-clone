from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Image,Comment
class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ('image', 'caption')
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('comment',)