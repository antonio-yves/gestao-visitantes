from django.contrib.auth.models import Permission
from rest_framework.generics import ListAPIView

from ..serializers import PermissionSerializer


class PermissionView(ListAPIView):
    serializer_class = PermissionSerializer

    def get_queryset(self):
        return Permission.objects.exclude(
            content_type_id__in=[1, 2, 4, 5],
        )
