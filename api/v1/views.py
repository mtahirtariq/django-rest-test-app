from rest_framework import authentication
from rest_framework import generics
from rest_framework import permissions

from api.v1 import serializers


class CreateCustomerView(generics.CreateAPIView):
    """View to create customer"""
    authentication_classes = (authentication.SessionAuthentication, )
    permission_classes = (permissions.AllowAny, )
    serializer_class = serializers.CustomerSerializer
