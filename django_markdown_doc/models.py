from django.db import models

# Create your models here.

from markdownx.models import MarkdownxField

class Document(models.Model):
    title = models.CharField(max_length=100)
    content = MarkdownxField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
