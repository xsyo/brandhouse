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

    role = models.CharField(max_length=2, choices=ROLE, default='MN', verbose_name='Роли')

