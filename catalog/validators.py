from django.forms import ValidationError


def text_validation(text: str):
    must_words = {'превосходно', 'роскошно'}
    if len(text.split()) < 2:
        raise ValidationError(f'Минимально необходимо 2 слова')

    lower_text = text.lower()
    for check_word in must_words:
        if check_word in lower_text:
            break
    else:
        raise ValidationError(f'Необходимо использовать одно из слов: {must_words}')
