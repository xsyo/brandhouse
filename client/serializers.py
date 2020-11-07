from rest_framework import serializers
from drf_writable_nested.serializers import WritableNestedModelSerializer

from .models import ClientProfile, Client


class ClientProfileSerializer(serializers.ModelSerializer):
    ''' Сериализатор профиля клиента '''

    class Meta:
        model = ClientProfile
        fields = ('id', 'name', 'company_name', 'city', 'phone_number', 
                'email', 'desired_budget', 'deadline', 'discount_subscription')


class ClientCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Client
        fields = ('username', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        password = validated_data.pop('password')

        clinet_obj = super().create(validated_data)

        clinet_obj.set_password(password)
        clinet_obj.save()

        return clinet_obj

