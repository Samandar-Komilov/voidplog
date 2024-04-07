from django import forms
from .models import Post


class PostCreateForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'subtitle', 'text', 'image', 'category']


class PostEditForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'subtitle', 'text', 'image', 'category']