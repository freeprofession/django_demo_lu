from django_filters.rest_framework import CharFilter, DateTimeFilter
from django_filters.rest_framework import FilterSet
from .models import Branch


class BranchInfoFilter(FilterSet):
    name = CharFilter(field_name='name', lookup_expr='icontains')

    class Meta:
        model = Branch
        fields = ['name']

