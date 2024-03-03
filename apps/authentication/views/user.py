from rest_framework.viewsets import ModelViewSet

from ..models import User
from ..serializers import UserGetSerializer, UserDefaultSerializer


class UserViewSet(ModelViewSet):
    lookup_field = 'uuid'

    def get_queryset(self):
        return User.objects.exclude(is_superuser=True).order_by('username')

    def get_serializer_class(self, *args, **kwargs):
        if self.action in ['list', 'retrieve']:
            return UserGetSerializer
        return UserDefaultSerializer
