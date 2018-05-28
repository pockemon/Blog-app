from django import forms
from . import models

class CreateArticle(forms.ModelForm):
    class Meta:
        #import model
        model = models.Article
        #fields that we want to output.
        fields = ['title', 'body', 'slug', 'thumb',]