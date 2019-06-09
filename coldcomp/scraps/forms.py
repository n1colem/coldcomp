from django import forms

from .models import Scrap

class ScrapForm(forms.ModelForm):

    class Meta:
        model = Scrap
        fields = ['title', 'author', 'body', 'mood']
