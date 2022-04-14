from django import forms
from django.forms import ChoiceField

from rating.models import Rating


class StarForm(forms.Form):
    star = ChoiceField(choices=Rating.choices)
