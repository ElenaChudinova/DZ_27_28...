from django import forms
from django.core.exceptions import ValidationError
from django.forms import ModelForm, BooleanField

from .models import Blog


class YourForm(forms.Form):
    forbidden_words = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция',
                       'радар', ]


class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for fild_name, fild in self.fields.items():
            if isinstance(fild, BooleanField):
                fild.widget.attrs['class'] = 'form-check-input'
            else:
                fild.widget.attrs['class'] = 'form-control'


class BlogForm(YourForm, StyleFormMixin, ModelForm):
    class Meta:
        model = Blog
        exclude = ("views_counter", "owner")

    def clean_blog_name(self):
        blog_name = self.cleaned_data['blog_name']
        for forbidden_word in self.forbidden_words:
            if forbidden_word in blog_name.lower():
                raise ValidationError('Запрещенное слово')

        return blog_name

class BlogModeratorForm(YourForm, StyleFormMixin, ModelForm):
    class Meta:
        model = Blog
        fields = ("publication", "blog_name", "description")