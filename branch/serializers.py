from rest_framework.serializers import SerializerMethodField
from globel_config.DynamicFieldsModelSerializer import DynamicFieldsModelSerializer
from .models import Branch, BranchHasAdminUser


class BranchInfoSerializers(DynamicFieldsModelSerializer):
    branch_has_user = SerializerMethodField()

    @staticmethod
    def get_branch_has_user(obj):
        if obj:
            return BranchHasUserSerializers(BranchHasAdminUser.objects.filter(flag=1, branch_id=obj.id), many=True, fields=('user_info',)).data
        else:
            return []

    class Meta:
        model = Branch
        fields = '__all__'


class BranchHasUserSerializers(DynamicFieldsModelSerializer):
    user_info = SerializerMethodField()

    @staticmethod
    def get_user_info(obj):
        return {
            'id': obj.admin_user.id,
            'name': obj.admin_user.name,
            'tel': obj.admin_user.tel
        }

    class Meta:
        model = BranchHasAdminUser
        fields = '__all__'
