from django.db import models
from django.contrib.auth import get_user_model
from phonenumber_field.modelfields import PhoneNumberField

from user.managers import UserManager

User = get_user_model()


class Manager(User):
    '''
    Прокси модель менеджера
    '''

    objects = UserManager(role='MN')

    def save(self, *args, **kwargs):
        self.role = 'MN'
        super().save(*args, **kwargs)

    class Meta:
        proxy = True
        verbose_name = 'Менеджер'
        verbose_name_plural = 'Менеджеры'


class ManagerProfile(models.Model):
    '''
    Профиль для манеджера
    '''

    user = models.OneToOneField(Manager, on_delete=models.CASCADE, related_name='managerProfile', verbose_name='Пользователь')
    phone_number = PhoneNumberField(verbose_name='Номер телефона')

    class Meta:
        verbose_name = 'Профиль менеджера'
        verbose_name_plural = 'Профили менеджеров'
