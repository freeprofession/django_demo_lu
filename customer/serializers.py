from rest_framework.serializers import SerializerMethodField
from globel_config.DynamicFieldsModelSerializer import DynamicFieldsModelSerializer
from .models import Customer, CustomerWallet, CustomerWalletRecord


class CustomerInfoSerializer(DynamicFieldsModelSerializer):

    class Meta:
        model = Customer
        fields = '__all__'


class CustomerWalletSerializer(DynamicFieldsModelSerializer):
    customer = SerializerMethodField()
    voucher = SerializerMethodField()

    @staticmethod
    def get_customer(obj):
        return {
            'uid': obj.customer.uid,
            'name': obj.customer.name
        }

    @staticmethod
    def get_voucher(obj):
        return {
            'id': obj.voucher.id,
            'name': obj.voucher.name,
            'num': obj.number,
            'worth': obj.voucher.worth
        }

    class Meta:
        model = CustomerWallet
        fields = '__all__'


class CustomerWalletHistorySerializer(DynamicFieldsModelSerializer):
    customer = SerializerMethodField()
    voucher = SerializerMethodField()
    admin_user = SerializerMethodField()
    branch = SerializerMethodField()

    @staticmethod
    def get_customer(obj):
        return {
            'uid': obj.customer.uid,
            'name': obj.customer.name
        }

    @staticmethod
    def get_voucher(obj):
        return {
            'id': obj.voucher.id,
            'name': obj.voucher.name,
        }

    @staticmethod
    def get_admin_user(obj):
        return {
            'id': obj.admin_user.id,
            'name': obj.admin_user.name,
        }

    @staticmethod
    def get_branch(obj):
        return {
            'id': obj.branch.id,
            'name': obj.branch.name,
        }

    class Meta:
        model = CustomerWalletRecord
        fields = '__all__'
