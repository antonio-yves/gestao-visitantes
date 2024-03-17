from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import PermissionView, GroupViewSet, UserViewSet

auth_routes = DefaultRouter()
auth_routes.register('group', GroupViewSet, basename='group')
auth_routes.register('user', UserViewSet, basename='user')


urlpatterns = [
    path('auth/permission/', PermissionView.as_view(), name='permission'),
    path('auth/', include(auth_routes.urls), name='auth'),
]
