from django import forms
from io import BytesIO
import os

from django.conf import settings
from django.core.files import temp as tempfile
from django.core.files.base import File


__all__ = ('UploadedFile')

class Leitor(forms.Form):
    text_area = forms.CharField(required=False, widget=forms.Textarea(attrs={'cols':55, 'rows':10}), label='')


class UploadFileForm(forms.Form):
    title = forms.CharField(max_length=50)
    file = forms.FileField()


