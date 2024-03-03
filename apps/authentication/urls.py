from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import UserViewSet

auth_routes = DefaultRouter()
auth_routes.register('user', UserViewSet, basename='user')


urlpatterns = [
    path('', include(auth_routes.urls), name='auth'),
]
