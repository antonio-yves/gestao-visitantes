import os
from uuid import uuid4

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill

def path_user_avatar(instance, filename):
    name, extension = os.path.splitext(filename)
    return '/'.join(['avatars', str(instance.uuid), f'avatar{extension}'])


class User(AbstractUser):
    # fields
    uuid = models.UUIDField(
        unique=True,
        default=uuid4,
        editable=False,
        db_index=True,
    )
    groups = models.ManyToManyField(
        to='auth.Group',
        verbose_name=_('groups'),
        blank=True,
        related_name='groups_user',
        related_query_name='user',
    )
    user_permissions = models.ManyToManyField(
        to='auth.Permission',
        verbose_name=_('permissions'),
        blank=True,
        related_name='permissions_user',
        related_query_name='user',
    )
    avatar = models.ImageField(
        verbose_name=_('avatar'),
        null=True,
        blank=True,
        upload_to=path_user_avatar,
    )
    avatar_thumb = ImageSpecField(
        source='avatar',
        processors=[ResizeToFill(200, 200)],
        format='JPEG',
        options={'quality': 60}
    )

    def __str__(self):
        return self.username

    class Meta:
        db_table = 'users'
        verbose_name = _('user')
        verbose_name_plural = _('users')
