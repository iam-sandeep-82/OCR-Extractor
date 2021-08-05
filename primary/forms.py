from django import forms
from django.forms.models import ModelForm
from .models import *
from django.utils.translation import ugettext_lazy as _

class FileForm(forms.ModelForm):
  class Meta:
    model=File
    fields=['photo',]
    widgets={
      'photo':forms.FileInput(attrs={'class':'inputfile', 'title': "Choose a image please"})
    }
    labels={
      'photo':_('Click me to upload image'),
    }


    # REFERENCES
    # labels = {
    #         'name': _('Writer'),
    #     }
    #     help_texts = {
    #         'name': _('Some useful help text.')
    #     }
    #     error_messages = {
    #         'name': {
    #             'max_length': _("This writer's name is too long."),
    #         },
    #     }


