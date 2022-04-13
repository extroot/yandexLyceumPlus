from django.forms import ModelForm

from rating.models import Rating


class StarForm(ModelForm):
    class Meta:
        model = Rating
        fields = ('star', )
