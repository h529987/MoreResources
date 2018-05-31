from django.shortcuts import render

# Create your views here.
from .models import normal_user, expert, administrator
from .serializers import NormalUserSerializer, ExpertSerializer, AdministratorSerializer
from rest_framework import viewsets, response
from rest_framework.decorators import api_view, renderer_classes

class NormalUserViewSet(viewsets.ModelViewSet):
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
	queryset = normal_user.objects.all()
	serializer_class = NormalUserSerializer