from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import static
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from drf_multiple_model.views import FlatMultipleModelAPIView
from django.shortcuts import get_object_or_404

from claim.models import Claim, ClaimWithDoc
from claim.serializers import ClaimSerializer, ClaimWithDocSerializer
from client.models import Client
from client.serializers import ClientCreateSerializer

from .models import Manager
from .serializers import ManagerSerializer, ManagerCreateSerializer
from .permissions import IsManager
from .utils import param_check, get_claim_class, get_client_profile_from_claim


class ManagerListCreateAPIView(ListCreateAPIView):
    ''' Контроллер для создания и просмотра списка менеджеров '''

    queryset = Manager.objects.all()
    serializer_class = ManagerCreateSerializer
    permission_classes = [IsAdminUser]


class ManagerRetrieveUpdateAPIView(RetrieveUpdateAPIView):
    ''' Личный кабинет менеджера '''

    queryset = Manager.objects.all()
    serializer_class = ManagerSerializer
    permission_classes = [IsAuthenticated, IsManager]


class ClaimListAPIView(FlatMultipleModelAPIView):
    ''' Контроллер для просмотра списка не оброботанных заявок '''

    sorting_fields = ['created_at']
    permission_classes = [IsAuthenticated, IsAdminUser | IsManager]

    querylist = [
        {
            'queryset': Claim.objects.filter(is_approved=None),
            'serializer_class': ClaimSerializer,
        },
        {
            'queryset': ClaimWithDoc.objects.filter(is_approved=None),
            'serializer_class': ClaimWithDocSerializer,
        }
    ]


class ClaimRetrieveUpdateAPIView(RetrieveUpdateAPIView):
    ''' Контроллер для отдельной заявки '''

    queryset = Claim.objects.all()
    serializer_class = ClaimSerializer
    permission_classes = [IsAuthenticated, IsManager]


@api_view(['POST'])
@permission_classes([IsAuthenticated, IsManager])
def reply_to_application(request, claim_id):
    ''' Контроллер для ответа заявки '''

    try:
        answer = param_check(request.data['answer'])
    except ValueError:
        return Response({'answer': 'answer должен быть true или false.'}, status=status.HTTP_400_BAD_REQUEST)
    
    try:
        doc = param_check(request.data['with_doc'])
    except ValueError:
        return Response({'with_doc': 'with_doc должен быть true или false.'}, status=status.HTTP_400_BAD_REQUEST)
    
    claim_class = get_claim_class(doc)

    claim_obj = get_object_or_404(claim_class, id=claim_id)

    claim_obj.is_approved = answer
    claim_obj.manager = request.user

    claim_obj.save()

    # TODO
    # Нужно реализовать уведомление на почту заказшика

    return Response({'return': 'success'})


class ClientCreateAPIView(CreateAPIView):
    ''' Контроллер для создания аккаунта клиента '''

    queryset = Client.objects.all()
    serializer_class = ClientCreateSerializer
    permission_classes = [IsAuthenticated, IsManager]

    def post(self, request, claim_id, *args, **kwargs):

        self.claim_id = claim_id

        return super().post(request, *args, **kwargs)

    def perform_create(self, serializer):
        clientProfile = get_client_profile_from_claim(self.claim_id)

        client_obj = serializer.save()

        clientProfile.user = client_obj
        clientProfile.save()


# TODO
# Создание модели технического задания
# Создать обработчики для технического задания