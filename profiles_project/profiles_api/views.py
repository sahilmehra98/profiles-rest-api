from django.shortcuts import render
from . import models
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from . import serializers
from rest_framework import status
from . import permissions
from rest_framework.authentication import TokenAuthentication

# Create your views here.
class UserProfileViewSet(viewsets.ModelViewSet):
    serializer_class=serializers.UserProfileSerializer
    queryset=models.UserProfile.objects.all()
    authentication_classes=(TokenAuthentication,)
    permission_classes=(permissions.UpdateOwnProfile,)
