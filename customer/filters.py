from django_filters.rest_framework import CharFilter, DateTimeFilter
from django_filters.rest_framework import FilterSet
from .models import Customer


class CustomerInfoFilter(FilterSet):
    name = CharFilter(field_name='name', lookup_expr='icontains')
    uid = CharFilter(field_name='uid', lookup_expr='icontains')
    time_start = DateTimeFilter(field_name='time_start', lookup_expr='gte')
    time_end = DateTimeFilter(field_name='time_end', lookup_expr='lte')

    class Meta:
        model = Customer
        fields = ['uid', 'name', 'time_start', 'time_end']

