from rest_framework import serializers

from core import models


class CustomerSerializer(serializers.ModelSerializer):
    """Serializer for Customer"""
    class Meta:
        model = models.Customer
        exclude = ()


class QuoteSerializer(serializers.ModelSerializer):
    """Serializer for quotes (in-active policies are considered quotes)"""
    state = serializers.ChoiceField(read_only=True, choices=models.Policy.State.choices)

    class Meta:
        model = models.Policy
        exclude = ('start_date', 'end_date')


class PolicySerializer(serializers.ModelSerializer):
    """Serializer for policies (quotes become policies after activation)"""
    class Meta:
        model = models.Policy
        exclude = ()
