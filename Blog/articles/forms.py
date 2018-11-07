from django import forms
from . import models
from django import forms
from pagedown.widgets import PagedownWidget


class CreateArticle(forms.ModelForm):
    body = forms.CharField(widget=PagedownWidget)

    class Meta:
        model = models.Article
        fields = ['lesson', 'title', 'body', 'slug', 'thumb', 'time']
