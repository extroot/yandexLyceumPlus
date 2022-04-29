from django.db import models
from django.db.models import UniqueConstraint

from users.models import CustomUser


class RatingManager(models.Manager):
    def get_user_star(self, item, user):
        user_star_if_exist = self.only('star').filter(item=item, user=user).first()
        if user_star_if_exist:
            return user_star_if_exist.star
        return 0


class Rating(models.Model):
    choices = (
        (5, 'Любовь'),
        (4, 'Обожание'),
        (3, 'Нейтрально'),
        (2, 'Неприязнь'),
        (1, 'Ненависть'),
        (0, 'Оценка отсутствует')
    )

    star = models.PositiveSmallIntegerField(verbose_name='Оценка', choices=choices, default=0)
    item = models.ForeignKey(
        verbose_name='Товар',
        to='catalog.Item',
        on_delete=models.CASCADE,
        related_name='ratings'
    )

    user = models.ForeignKey(
        verbose_name='Пользователь',
        to=CustomUser,
        on_delete=models.CASCADE,
        related_name='ratings'
    )

    objects = RatingManager()

    class Meta:
        verbose_name = 'Оценка'
        verbose_name_plural = 'Оценки'
        constraints = [
            UniqueConstraint(
                name='rating_unique',
                fields=('item', 'user')
            )
        ]
