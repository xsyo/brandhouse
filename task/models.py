from django.db import models
from django.core.validators import MinValueValidator

from user.models import User
from manager.models import Manager
from client.models import Client

from .utils import get_today


class Project(models.Model):
    ''' Модель проекта '''

    STATUS = (
        ('DV', 'Developing'),
        ('CM', 'Completed'),
        ('SS', 'Suspended'),
    )

    name = models.CharField(max_length=255, verbose_name='Название проекта')
    manager = models.ForeignKey(Manager, related_name='projects', null=True, 
                                on_delete=models.SET_NULL, verbose_name='Ответсвенный менеджер')
    client = models.OneToOneField(Client, related_name='project', null=True, 
                                on_delete=models.SET_NULL, verbose_name='Заказчик')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата и время создания проекта')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата и время обновления проекта')
    deadline = models.DateField(verbose_name='Дата сдачи проекта', validators=[MinValueValidator(get_today),])
    status = models.CharField(max_length=2, choices=STATUS, default='DV', verbose_name='Статус проекта')

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['deadline', 'created_at', 'updated_at']
        verbose_name = 'Проект'
        verbose_name_plural = 'Проекты'


class Task(models.Model):
    ''' Модель задания '''

    name = models.CharField(max_length=255, verbose_name='Название задания')
    project = models.ForeignKey(Project, related_name='tasks', on_delete=models.CASCADE, verbose_name='Проект')
    executor = models.ForeignKey(User, related_name='my_tasks', null=True, 
                        on_delete=models.SET_NULL, verbose_name='Исполнитель')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Задание'
        verbose_name_plural = 'Задания'


class SubTask(models.Model):
    ''' Модель подзадачи '''

    task = models.ForeignKey(Task, related_name='subtasks', on_delete=models.CASCADE, verbose_name='Задание')
    name = models.CharField(max_length=255, verbose_name='Название подзадачи')
    is_done = models.BooleanField(default=False, verbose_name='Выполнена ли подзадача')
    description = models.TextField(verbose_name='Описание')
    
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Подзадача'
        verbose_name_plural = 'Подзадачи'