from rest_framework import serializers

from core import models


class CustomerSerializer(serializers.ModelSerializer):
    """Serializer for Customer"""
    class Meta:
        model = models.Customer
        exclude = ()
