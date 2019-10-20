from django.shortcuts import render
from . import models
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from . import serializers
from rest_framework import status
from . import permissions
from rest_framework.authentication import TokenAuthentication
from rest_framework import filters
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.permissions import IsAuthenticated

# Create your views here.
class UserProfileViewSet(viewsets.ModelViewSet):
    serializer_class=serializers.UserProfileSerializer
    queryset=models.UserProfile.objects.all()
    authentication_classes=(TokenAuthentication,)
    permission_classes=(permissions.UpdateOwnProfile,)
    filter_backends=(filters.SearchFilter,)
    search_fields=('name','email',)

class LoginViewSet(viewsets.ViewSet):
    serializer_class=AuthTokenSerializer

    def create(self,request):
        return ObtainAuthToken().post(request)

class UserProfileFeedViewSet(viewsets.ModelViewSet):
    serializer_class=serializers.ProfileFeedSerializer
    authentication_classes=(TokenAuthentication,)
    queryset=models.ProfileFeedItem.objects.all()
    permission_classes=(permissions.PostOwnStatus,IsAuthenticated)

    def perform_create(self,serializer):
        serializer.save(user_profile=self.request.user)
