from django import forms
from .models import Post, Comment


class PostCreateForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'subtitle', 'text', 'image', 'category']


class PostEditForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'subtitle', 'text', 'image', 'category']

    
class CommentCreateForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name']