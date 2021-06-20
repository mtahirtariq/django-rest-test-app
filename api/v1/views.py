from http import HTTPStatus

import django_filters.rest_framework
from rest_framework import authentication
from rest_framework import decorators
from rest_framework import mixins
from rest_framework import permissions
from rest_framework import viewsets
from rest_framework.response import Response

from core import models
from . import filters
from . import serializers


class CustomerViewSet(mixins.CreateModelMixin, mixins.ListModelMixin, viewsets.GenericViewSet):
    """View to create customer"""
    authentication_classes = (authentication.SessionAuthentication, )
    permission_classes = (permissions.AllowAny, )
    serializer_class = serializers.CustomerSerializer
    queryset = models.Customer.objects.all()
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filter_class = filters.CustomerFilter


class QuoteViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    """
    ViewSet to read/search Policy model. Only in-active policies (which are considered quotes)
    can be retrieved though this viewset.
    """
    authentication_classes = (authentication.SessionAuthentication,)
    permission_classes = (permissions.AllowAny,)
    serializer_class = serializers.QuoteSerializer
    queryset = models.Policy.objects.exclude(state=models.Policy.State.ACTIVE)

    @decorators.action(methods=['POST'], detail=True)
    def accept(self, request, *args, **kwargs):
        """
        Marks quote as accepted. It has been separated from update
        (POST) method so that permissions can be controlled.
        """
        obj = self.get_object()
        obj.state = models.Policy.State.ACCEPTED
        obj.save()
        serializer = self.get_serializer(instance=obj)
        return Response(data=serializer.data, status=HTTPStatus.OK)

    @decorators.action(methods=['POST'], detail=True, url_path='payment-complete')
    def payment_complete(self, request, *args, **kwargs):
        """
        Marks quote as active (converts to policy). It has been separated from update
        (POST) method so that permissions can be controlled.
        """
        obj = self.get_object()
        obj.state = models.Policy.State.ACTIVE
        obj.save()
        serializer = self.get_serializer(instance=obj)
        return Response(data=serializer.data, status=HTTPStatus.OK)


class PolicyViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    """ViewSet to read/search Policy model. Only active policies can be retrieved though this viewset."""
    authentication_classes = (authentication.SessionAuthentication,)
    permission_classes = (permissions.AllowAny,)
    serializer_class = serializers.PolicySerializer
    queryset = models.Policy.objects.filter(state=models.Policy.State.ACTIVE)
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_fields = ['customer']
