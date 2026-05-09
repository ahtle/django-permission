from rest_framework import status
from rest_framework.response import Response
from api.base import PermissionAPIView
from core.definitions import PD


class ListAgentView(PermissionAPIView):
    permissions = [PD.can_view_agent]

    def get(self, request):
        return Response([], status=status.HTTP_200_OK)
