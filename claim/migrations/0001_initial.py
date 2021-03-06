# Generated by Django 3.1.2 on 2020-10-30 11:50

import claim.utils
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('manager', '0001_initial'),
        ('client', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Design',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('style', models.CharField(choices=[('Flat', 'Flat стиль'), ('Metro', 'Metro стиль'), ('Material Design', 'Material Design'), ('Minimalistic', 'Минималистичный'), ('Classic', 'Классический'), ('Cartoon', 'Мультипликационный'), ('Retro', 'Ретро'), ('Futuristic', 'Футуристический'), ('Business', 'Бизнес'), ('Other', 'Другой')], max_length=25, verbose_name='Стиль дизайна')),
                ('layout_type', models.CharField(choices=[('Adaptive', 'Адаптивный'), ('Fixed', 'Фиксированный'), ('Rubber', 'Резиновый'), ('Other', 'Другой')], max_length=20, verbose_name='Тип макета')),
                ('layout_structure', models.URLField(blank=True, verbose_name='Структура макета')),
                ('characteristic', models.TextField(verbose_name='Слова характерезующие ваш сайт')),
                ('liked_sites', models.TextField(verbose_name='Сайты, которые вам нравятся')),
                ('disliked_sites', models.TextField(blank=True, verbose_name='Сайты, которые вам не нравятся')),
                ('color_spectrum', models.TextField(blank=True, verbose_name='Цветовая гамма')),
                ('need_logo', models.BooleanField(verbose_name='Нужен ли логотип')),
                ('additional_information', models.TextField(blank=True, verbose_name='Дополнительная информация')),
            ],
            options={
                'verbose_name': 'Дизайн заказа',
                'verbose_name_plural': 'Дизайны заказов',
            },
        ),
        migrations.CreateModel(
            name='Functional',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('languages', models.TextField(verbose_name='Языки')),
                ('control_system', models.BooleanField(blank=True, default=False, verbose_name='Система управления')),
                ('need_domain', models.BooleanField(blank=True, default=False, verbose_name='Необходим ли домен')),
                ('domain_name', models.CharField(blank=True, max_length=255, verbose_name='Доменное имя')),
                ('news', models.BooleanField(blank=True, default=False, verbose_name='Новостей')),
                ('static', models.BooleanField(blank=True, default=False, verbose_name='Статические страницы')),
                ('blog', models.BooleanField(blank=True, default=False, verbose_name='Блог')),
                ('feedback', models.BooleanField(blank=True, default=False, verbose_name='Обратная связь')),
                ('media', models.BooleanField(blank=True, default=False, verbose_name='Фото/видео галерея')),
                ('catalog', models.BooleanField(blank=True, default=False, verbose_name='Каталог товаров')),
                ('order_form', models.BooleanField(blank=True, default=False, verbose_name='Форма заказа')),
                ('site_reviews', models.BooleanField(blank=True, default=False, verbose_name='Отзывы о сайте')),
                ('user_account', models.BooleanField(blank=True, default=False, verbose_name='Аккаунт пользователя')),
                ('subscribe_to_news', models.BooleanField(blank=True, default=False, verbose_name='Подписка на новости')),
                ('online_payments', models.BooleanField(blank=True, default=False, verbose_name='Онлайн платежи')),
                ('rotation_of_banners', models.BooleanField(blank=True, default=False, verbose_name='Ротация баннеров')),
                ('search', models.BooleanField(blank=True, default=False, verbose_name='Поиск')),
                ('FAQ', models.BooleanField(blank=True, default=False, verbose_name='FAQ (Вопросы и ответы)')),
                ('shopping_cart', models.BooleanField(blank=True, default=False, verbose_name='Корзина товаров')),
                ('SMS_connection', models.BooleanField(blank=True, default=False, verbose_name='Подключение SMS')),
                ('working_with_third_party_API', models.BooleanField(blank=True, default=False, verbose_name='Работа со сторонним API')),
                ('working_with_the_Steam_API', models.BooleanField(blank=True, default=False, verbose_name='Работа со Steam API')),
                ('The_core_of_the_service_project', models.BooleanField(blank=True, default=False, verbose_name='Ядро сервисного проекта')),
                ('balance_replenishment', models.BooleanField(blank=True, default=False, verbose_name='Пополнение баланса')),
                ('promo_codes', models.BooleanField(blank=True, default=False, verbose_name='Промо коды')),
                ('social_authorization_networks', models.BooleanField(blank=True, default=False, verbose_name='Авторизация через соц. сети')),
            ],
            options={
                'verbose_name': 'Функционал заказа',
                'verbose_name_plural': 'Функционалы заказов',
            },
        ),
        migrations.CreateModel(
            name='ClaimWithDoc',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата и время подачи заявки')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Дата и время обновления заявки')),
                ('is_approved', models.BooleanField(blank=True, null=True, verbose_name='Одобрено ли заявка')),
                ('document', models.FileField(upload_to=claim.utils.claim_doc_uploader, verbose_name='Файл технического задания')),
                ('client', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='client.clientprofile', verbose_name='Информация о клиенте')),
                ('manager', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='claims_with_doc', to='manager.manager', verbose_name='Ответсвенный менеджер')),
            ],
            options={
                'verbose_name': 'Заявка с документом',
                'verbose_name_plural': 'Заявки с документом',
                'ordering': ['created_at', 'updated_at'],
            },
        ),
        migrations.CreateModel(
            name='Claim',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата и время подачи заявки')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Дата и время обновления заявки')),
                ('is_approved', models.BooleanField(blank=True, null=True, verbose_name='Одобрено ли заявка')),
                ('client', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='client.clientprofile', verbose_name='Информация о клиенте')),
                ('design', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='claim', to='claim.design', verbose_name='Задание по дизайну')),
                ('functional', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='claim', to='claim.functional', verbose_name='Задание по функциональности')),
                ('manager', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='claims', to='manager.manager', verbose_name='Ответсвенный менеджер')),
            ],
            options={
                'verbose_name': 'Заявка',
                'verbose_name_plural': 'Заявки',
                'ordering': ['created_at', 'updated_at'],
            },
        ),
    ]
