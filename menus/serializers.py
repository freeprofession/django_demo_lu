from rest_framework.serializers import SerializerMethodField
from globel_config.DynamicFieldsModelSerializer import DynamicFieldsModelSerializer
from .models import Menu, MenuHasPermission, RoleHasMenu


class MenusInfoSerializer(DynamicFieldsModelSerializer):
    child_menu = SerializerMethodField()
    role_list = SerializerMethodField()
    permission_list = SerializerMethodField()
    show_state = SerializerMethodField()

    @staticmethod
    def get_child_menu(obj):
        return MenusInfoSerializer(Menu.objects.filter(flag=1, before_menu_id=obj.id, show=1), many=True,
                                   fields=('id', 'role_list', 'permission_list', 'show_state',
                                           'name', 'page_url', 'page_name', 'icon', 'flag')).data

    @staticmethod
    def get_role_list(obj):
        return RoleHasMenuSerializer(RoleHasMenu.objects.filter(flag=1, menu_id=obj.id), many=True,
                                     fields=('role_info',)).data

    @staticmethod
    def get_permission_list(obj):
        return MenuHasPermissionSerializer(MenuHasPermission.objects.filter(flag=1, menu_id=obj.id), many=True,
                                           fields=('menu_info',)).data

    @staticmethod
    def get_show_state(obj):
        if obj.show == 1:
            return '显示'
        elif obj.show == 0:
            return '隐藏'
        return '状态异常'

    class Meta:
        model = Menu
        fields = '__all__'


class MenuHasPermissionSerializer(DynamicFieldsModelSerializer):
    permission_info = SerializerMethodField()
    menu_info = SerializerMethodField()

    @staticmethod
    def get_permission_info(obj):
        return {
            'id': obj.permission.id,
            'name': obj.permission.name,
        }

    @staticmethod
    def get_menu_info(obj):
        return {
            'id': obj.menu.id,
            'name': obj.menu.name,
        }

    class Meta:
        model = MenuHasPermission
        fields = '__all__'


class RoleHasMenuSerializer(DynamicFieldsModelSerializer):
    role_info = SerializerMethodField()
    menu_info = SerializerMethodField()

    @staticmethod
    def get_menu_info(obj):
        return {
            'id': obj.menu.id,
            'name': obj.menu.name,
        }

    @staticmethod
    def get_role_info(obj):
        return {
            'id': obj.role.id,
            'name': obj.role.name
        }

    class Meta:
        model = RoleHasMenu
        fields = '__all__'
