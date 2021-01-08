from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    ''' Модель пользователя '''

    ROLE = (
        ('MN', 'Manager'),
        ('CL', 'Client'),
        ('BK', 'Backend'),
        ('FT', 'Frontend'),
        ('DR', 'Designer'),
    )

    def __str__(self):
        return self.first_name

    role = models.CharField(max_length=2, choices=ROLE, default='MN', verbose_name='Роли')

