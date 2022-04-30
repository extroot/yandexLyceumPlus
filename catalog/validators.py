from django.forms import ValidationError
from django.utils.html import strip_tags


def text_validation(text: str):
    must_words = {'превосходно', 'роскошно'}
    if len(text.split()) < 2:
        raise ValidationError('Минимально необходимо 2 слова')
    lower_text = set(strip_tags(text).lower().split())
    if len(lower_text) == len(lower_text - must_words):
        raise ValidationError(f'Необходимо использовать одно из слов: {must_words}')
