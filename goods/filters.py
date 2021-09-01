from django_filters.rest_framework import CharFilter, DateTimeFilter
from django_filters.rest_framework import FilterSet
from .models import Goods


class GoodsInfoFilter(FilterSet):
    name = CharFilter(field_name='name', lookup_expr='icontains')
    uuid = CharFilter(field_name='uuid', lookup_expr='icontains')

    class Meta:
        model = Goods
        fields = ['uuid', 'name']

