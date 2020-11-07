from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAdminUser
from drf_multiple_model.views import FlatMultipleModelAPIView

from .models import Claim, ClaimWithDoc
from .serializers import ClaimSerializer, ClaimWithDocSerializer


class ClaimCreateAPIView(CreateAPIView):
    ''' Контроллер для создания заявки '''

    queryset = Claim.objects.all()
    serializer_class = ClaimSerializer


class ClaimWithDocCreateView(CreateAPIView):
    ''' Контроллер для создания заявки с документом '''

    queryset = ClaimWithDoc.objects.all()
    serializer_class = ClaimWithDocSerializer


