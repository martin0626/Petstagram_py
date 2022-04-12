import os
from os.path import join

from django import forms

from petstagramFinal import settings
from petstagramFinal.pets.models import Pet, Comment


class BootsTrapMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_bootstrap()

    def _init_bootstrap(self):
        for (_, field) in self.fields.items():
            if 'class' not in field.widget.attrs:
                field.widget.attrs['class'] = ''
            field.widget.attrs['class'] += ' form-control'


class PetForm(BootsTrapMixin, forms.ModelForm):

    class Meta:
        model = Pet
        exclude = ['user']


class EditForm(PetForm):

    class Meta:
        model = Pet
        exclude = ['user']
        widgets = {
            'type': forms.TextInput(
                attrs={
                    "readonly": "readonly",
                }
            )
        }


class CommentsForm(forms.Form):
    text = forms.CharField(
        widget=forms.Textarea(
            attrs={
                'class': 'form-control rounded 2'
            }
        )
    )

