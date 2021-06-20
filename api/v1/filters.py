from django.db.models import Q
from django_filters import filterset

from core import models


class CustomerFilter(filterset.FilterSet):
    """FilterSet class to customize search for customer"""

    name = filterset.CharFilter(method='filter_by_name')
    policy_type = filterset.CharFilter(method='filter_by_policy_type')

    @staticmethod
    def filter_by_name(queryset, _, value):
        """Perform case-insensitive containment search for value in first_name and last_name fields"""
        if value:
            queryset = queryset.filter(Q(first_name__icontains=value) | Q(last_name__icontains=value))
        return queryset

    @staticmethod
    def filter_by_policy_type(queryset, _, value):
        """Perform case-insensitive exact search for value for policy_type"""
        if value:
            queryset = queryset.filter(policies__type__iexact=value)
        return queryset

    class Meta:
        model = models.Customer
        fields = {
            'dob': ['exact'],
        }
