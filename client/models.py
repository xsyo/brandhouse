from django.db import models
from django.contrib.auth import get_user_model
from phonenumber_field.modelfields import PhoneNumberField

from user.managers import UserManager


User = get_user_model()

class Client(User):
    ''' Прокси модель клиента '''

    objects = UserManager(role='CL')

    def save(self, *args, **kwargs):
        self.role = 'CL'
        super().save(*args, **kwargs)

    class Meta:
        proxy = True
        verbose_name = 'Клиенты'
        verbose_name_plural = 'Клиент'



class ClientProfile(models.Model):
    ''' Профиль для клиента '''

    user = models.OneToOneField(Client, blank=True, null=True, 
                                on_delete=models.SET_NULL, 
                                related_name='clientProfile', verbose_name='Пользователь')
    name = models.CharField(max_length=255, verbose_name='Ф.И.О.')
    company_name = models.CharField(max_length=255, blank=True, verbose_name='Название компании')
    city = models.CharField(max_length=255, verbose_name='Страна, Город')
    phone_number = PhoneNumberField(verbose_name='Номер телефона')
    email = models.EmailField(verbose_name='Email')
    desired_budget = models.DecimalField(max_digits=10, decimal_places=2, 
                                        blank=True, null=True, verbose_name='Желаемый бюджет')
    deadline = models.DateField(blank=True, null=True, verbose_name='Срок разработки')
    discount_subscription = models.BooleanField(blank=True, default=False, verbose_name='Подписка на скидки')


    class Meta:
        verbose_name = 'Профиль клиента'
        verbose_name_plural = 'Профили клиентов'
