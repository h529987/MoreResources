from django.shortcuts import render

# Create your views here.
from .models import normal_user, expert, administrator
from .serializers import NormalUserSerializer, ExpertSerializer, AdministratorSerializer
from rest_framework import viewsets, response
from rest_framework.decorators import api_view, renderer_classes
"""
    retrieve:
        Return a user instance.

    list:
        Return all users, ordered by most recently joined.

    create:
        Create a new user.

    delete:
        Remove an existing user.

    partial_update:
        Update one or more fields on an existing user.

    update:
        Update a user.
"""
class NormalUserViewSet(viewsets.ModelViewSet):
	queryset = normal_user.objects.all()
	serializer_class = NormalUserSerializer

class ExpertViewSet(viewsets.ModelViewSet):
    queryset = expert.objects.all()
    serializer_class = ExpertSerializer

class AdministratorViewSet(viewsets.ModelViewSet):
    queryset = administrator.objects.all()
    serializer_class = AdministratorSerializer