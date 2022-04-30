from datetime import date

from .models import Profile


def birthdays_today(request):
    today_date = date.today()
    having_a_birthday = Profile.objects.filter(
        birthday__month=today_date.month,
        birthday__day=today_date.day
    ).only(
        'birthday', 'user__first_name')
    context = {
        'birthdays': having_a_birthday,
    }
    return context
