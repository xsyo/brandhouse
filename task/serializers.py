from rest_framework import serializers

from drf_writable_nested.serializers import WritableNestedModelSerializer

from .models import SubTask, Task, Project


class SubTaskSerializer(serializers.ModelSerializer):
    ''' Сериализатор подзадачи '''

    class Meta:
        model = SubTask
        fields = ('id', 'task', 'name', 'is_done', 'description')
        read_only_fields = ('is_done',)


class TaskSerializer(WritableNestedModelSerializer):

    subtasks = SubTaskSerializer(many=True)
    executor = serializers.StringRelatedField()

    class Meta:
        model = Task
        fields = ('id', 'executor', 'project', 'name', 'subtasks')


class ProjectSerializer(WritableNestedModelSerializer):

    tasks = TaskSerializer(many=True)

    class Meta:
        model = Project
        fields = ('id', 'name', 'manager', 'client', 'created_at', 'updated_at', 'deadline', 'status', 'tasks')
        read_only_fields = ('status',)


