from django.contrib.auth.validators import UnicodeUsernameValidator
from django.db import models
from django.utils.translation import gettext_lazy as _
from rest_framework import serializers

from ..models import User


class UserGetSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = (
            'uuid', 'first_name', 'last_name', 'username',
            'email', 'avatar', 'date_joined',
        )


class UserDefaultSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(
        allow_blank=False,
        allow_null=False,
        required=True,
    )
    last_name = serializers.CharField(
        allow_blank=False,
        allow_null=False,
        required=True,
    )
    username = serializers.CharField(
        allow_blank=False,
        allow_null=False,
        required=True,
        validators=[UnicodeUsernameValidator(),],
    )
    email = serializers.EmailField(
        allow_blank=False,
        allow_null=False,
        required=True,
    )

    class Meta:
        model = User
        fields = (
            'uuid', 'first_name', 'last_name', 'username',
            'email', 'avatar',
        )

    def validate_username(self, value):
        try:
            User.objects.get(username=value)
            raise serializers.ValidationError(_('Username is already in use'))
        except models.ObjectDoesNotExist:
            return value
