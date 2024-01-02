
from django import forms
from markdownx.fields import MarkdownxFormField
from .models import Document

class DocumentForm(forms.ModelForm):
    content = MarkdownxFormField()

    class Meta:
        model = Document
        fields = ['title', 'content']