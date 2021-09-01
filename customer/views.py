from rest_framework.views import APIView
from globel_config.ListApiView import ListApiView
from rest_framework.pagination import PageNumberPagination
from django.db.models import Q
from django_filters.rest_framework import DjangoFilterBackend
from .models import Customer, CustomerWallet, CustomerWalletRecord
from .serializers import CustomerInfoSerializer, CustomerWalletSerializer, CustomerWalletHistorySerializer
from .filters import CustomerInfoFilter


class CustomerInfoListView(ListApiView):
    serializer_class = CustomerInfoSerializer
    pagination_class = PageNumberPagination
    queryset = Customer.objects.filter(~Q(flag=0)).order_by('-id')
    fields = ['id', 'uid', 'name', 'tel', 'avatar', 'time_create', 'flag']
    filter_backends = (DjangoFilterBackend, )
    filter_class = CustomerInfoFilter


class CustomerWalletListView(ListApiView):
    serializer_class = CustomerWalletSerializer
    fields = ['id', 'customer', 'voucher', 'all_worth', 'flag']
    filter_backends = (DjangoFilterBackend,)

    def get_queryset(self):
        if 'uid' in self.request.query_params:
            uid = self.request.query_params['uid']
            return CustomerWallet.objects.filter(~Q(flag=0), customer__uid=uid).order_by('-time_create')
        return CustomerWallet.objects.none()


class CustomerWalletHistoryListView(ListApiView):
    serializer_class = CustomerWalletHistorySerializer
    fields = ['id', 'customer', 'voucher', 'value', 'admin_user', 'branch', 'time_create', 'flag']
    pagination_class = PageNumberPagination
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ['customer__uid', 'voucher__name']

    def get_queryset(self):
        if 'customer__uid' in self.request.query_params:
            return CustomerWalletRecord.objects.filter(~Q(flag=0)).order_by('-time_create')
        return CustomerWallet.objects.none()
