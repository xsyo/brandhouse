from rest_framework.generics import RetrieveAPIView
from rest_framework.permissions import IsAuthenticated

from task.models import Project
from task.serializers import ProjectSerializer

from .permissions import IsClient


class ProjectRetrieveAPIView(RetrieveAPIView):

    queryset = Project.objects.all()
    serializer_class = ProjectSerializer()
    permission_classes = [IsAuthenticated, IsClient]

