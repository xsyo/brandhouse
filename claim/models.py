from django.db import models

from client.models import ClientProfile
from manager.models import Manager

from .utils import claim_doc_uploader



class Design(models.Model):
    '''
    Модель перечня дизайна
    '''

    DESIGN_STYLE = (
        ('Flat', 'Flat стиль'),
        ('Metro', 'Metro стиль'),
        ('Material Design', 'Material Design'),
        ('Minimalistic', 'Минималистичный'),
        ('Classic', 'Классический'),
        ('Cartoon', 'Мультипликационный'),
        ('Retro', 'Ретро'),
        ('Futuristic', 'Футуристический'),
        ('Business', 'Бизнес'),
        ('Other', 'Другой'),
    )

    LAYOUT_TYPE = (
        ('Adaptive', 'Адаптивный'),
        ('Fixed', 'Фиксированный'),
        ('Rubber', 'Резиновый'),
        ('Other', 'Другой'),
    )

    style = models.CharField(max_length=25, choices=DESIGN_STYLE, verbose_name='Стиль дизайна')
    layout_type = models.CharField(max_length=20, choices=LAYOUT_TYPE, verbose_name='Тип макета')
    layout_structure = models.URLField(blank=True, verbose_name='Структура макета')
    characteristic = models.TextField(verbose_name='Слова характерезующие ваш сайт')
    liked_sites = models.TextField(verbose_name='Сайты, которые вам нравятся')
    disliked_sites = models.TextField(blank=True, verbose_name='Сайты, которые вам не нравятся')
    color_spectrum = models.TextField(blank=True, verbose_name='Цветовая гамма')
    need_logo = models.BooleanField(verbose_name='Нужен ли логотип')
    additional_information = models.TextField(blank=True, verbose_name='Дополнительная информация')

    class Meta:
        verbose_name = 'Дизайн заказа'
        verbose_name_plural = 'Дизайны заказов'


class Functional(models.Model):
    '''
    Модель перечня функциональности
    '''

    languages = models.TextField(verbose_name='Языки')
    control_system = models.BooleanField(blank=True, default=False, verbose_name='Система управления')
    need_domain = models.BooleanField(blank=True, default=False, verbose_name='Необходим ли домен')
    domain_name = models.CharField(max_length=255, blank=True, verbose_name='Доменное имя')
    news = models.BooleanField(blank=True, default=False, verbose_name='Новостей')
    static = models.BooleanField(blank=True, default=False, verbose_name='Статические страницы')
    blog = models.BooleanField(blank=True, default=False, verbose_name='Блог')
    feedback = models.BooleanField(blank=True, default=False, verbose_name='Обратная связь')
    media = models.BooleanField(blank=True, default=False, verbose_name='Фото/видео галерея')
    catalog = models.BooleanField(blank=True, default=False, verbose_name='Каталог товаров')
    order_form = models.BooleanField(blank=True, default=False, verbose_name='Форма заказа')
    site_reviews = models.BooleanField(blank=True, default=False, verbose_name='Отзывы о сайте')
    user_account = models.BooleanField(blank=True, default=False, verbose_name='Аккаунт пользователя')
    subscribe_to_news = models.BooleanField(blank=True, default=False, verbose_name='Подписка на новости')
    online_payments = models.BooleanField(blank=True, default=False, verbose_name='Онлайн платежи')
    rotation_of_banners = models.BooleanField(blank=True, default=False, verbose_name='Ротация баннеров')
    search = models.BooleanField(blank=True, default=False, verbose_name='Поиск')
    FAQ = models.BooleanField(blank=True, default=False, verbose_name='FAQ (Вопросы и ответы)')
    shopping_cart = models.BooleanField(blank=True, default=False, verbose_name='Корзина товаров')
    SMS_connection = models.BooleanField(blank=True, default=False, verbose_name='Подключение SMS')
    working_with_third_party_API = models.BooleanField(blank=True, default=False, verbose_name='Работа со сторонним API')
    working_with_the_Steam_API = models.BooleanField(blank=True, default=False, verbose_name='Работа со Steam API')
    The_core_of_the_service_project = models.BooleanField(blank=True, default=False, verbose_name='Ядро сервисного проекта')
    balance_replenishment = models.BooleanField(blank=True, default=False, verbose_name='Пополнение баланса')
    promo_codes = models.BooleanField(blank=True, default=False, verbose_name='Промо коды')
    social_authorization_networks = models.BooleanField(blank=True, default=False, verbose_name='Авторизация через соц. сети')

    class Meta:
        verbose_name = 'Функционал заказа'
        verbose_name_plural = 'Функционалы заказов'


class AbstractClaim(models.Model):
    '''
    Абстрактная модель заявки
    '''

    client = models.OneToOneField(ClientProfile, on_delete=models.CASCADE, verbose_name='Информация о клиенте')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата и время подачи заявки')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата и время обновления заявки')
    is_approved = models.BooleanField(blank=True, null=True, verbose_name='Одобрено ли заявка')
    

    class Meta:
        abstract = True


class Claim(AbstractClaim):
    '''
    Модель заявки
    '''

    design = models.OneToOneField(Design, on_delete=models.CASCADE, related_name='claim', verbose_name='Задание по дизайну')
    functional = models.OneToOneField(Functional, on_delete=models.CASCADE, related_name='claim', verbose_name='Задание по функциональности')
    manager = models.ForeignKey(Manager, on_delete=models.SET_NULL, related_name='claims',
                                null=True, default=None, verbose_name='Ответсвенный менеджер')

    class Meta:
        ordering = ['created_at', 'updated_at']
        verbose_name = 'Заявка'
        verbose_name_plural = 'Заявки'


class ClaimWithDoc(AbstractClaim):
    '''
    Модель заявки со своим техническим заданием
    '''

    document = models.FileField(upload_to=claim_doc_uploader, verbose_name='Файл технического задания')
    manager = models.ForeignKey(Manager, on_delete=models.SET_NULL, related_name='claims_with_doc',
                                null=True, default=None, verbose_name='Ответсвенный менеджер')

    class Meta:
        ordering = ['created_at', 'updated_at']
        verbose_name = 'Заявка с документом'
        verbose_name_plural = 'Заявки с документом'