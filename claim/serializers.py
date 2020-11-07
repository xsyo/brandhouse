from rest_framework import serializers
from drf_writable_nested.serializers import WritableNestedModelSerializer

from client.serializers import ClientProfileSerializer
from client.models import ClientProfile

from .models import Design, Functional, Claim, ClaimWithDoc


class DesignSerializer(serializers.ModelSerializer):
    ''' Сериализатор модели дизайна заявки '''

    class Meta:
        model = Design
        fields = '__all__'


class FunctionalSerializer(serializers.ModelSerializer):
    ''' Сериализатор модели функционала дизайна '''

    class Meta:
        model = Functional
        fields = '__all__'


class ClaimSerializer(WritableNestedModelSerializer):
    ''' Сериализатор модели заявки '''

    client = ClientProfileSerializer()
    design = DesignSerializer()
    functional = FunctionalSerializer()

    class Meta:
        model = Claim
        fields = ('client', 'design', 'functional', 'created_at', 'updated_at', 'is_approved')
        read_only_fields = ('created_at', 'updated_at', 'is_approved')
    

class ClaimWithDocSerializer(WritableNestedModelSerializer):
    ''' Сериализатор модели заявки с документом '''
    
    client = ClientProfileSerializer()

    class Meta:
        model = ClaimWithDoc
        fields = ('client', 'document', 'created_at', 'updated_at', 'is_approved')
        read_only_fields = ('created_at', 'updated_at', 'is_approved')