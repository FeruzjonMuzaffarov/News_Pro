from django import forms
from users.models import Comment
from .models import Contact

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'message']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']

