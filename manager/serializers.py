from rest_framework import serializers
from drf_writable_nested.serializers import WritableNestedModelSerializer

from .models import Manager, ManagerProfile


class ManagerProfileSerializer(serializers.ModelSerializer):
    ''' Сериализатор профиля менеджера '''

    class Meta:
        model = ManagerProfile
        fields = ('phone_number',)

class ManagerSerializer(WritableNestedModelSerializer):
    ''' Сериализатор модели менеджера '''
    
    managerProfile = ManagerProfileSerializer()

    class Meta:
        model = Manager
        fields = ('id', 'username', 'email', 'first_name', 'role', 'managerProfile')
        read_only_fields = ('role',)


class ManagerCreateSerializer(WritableNestedModelSerializer):
    ''' Сериализатор для создания модели менеджера '''
    
    managerProfile = ManagerProfileSerializer()

    class Meta:
        model = Manager
        fields = ('username', 'email', 'first_name', 'password', 'managerProfile')
        extra_kwargs = {'password': {'write_only': True}}
    
    def create(self, validated_data):
        password = validated_data.pop('password')

        new_manager = super().create(validated_data)

        new_manager.set_password(password)
        new_manager.save()

        return new_manager