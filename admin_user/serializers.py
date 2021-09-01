from rest_framework.serializers import SerializerMethodField
from django.db.models import Q
from django.utils import timezone
from globel_config.DynamicFieldsModelSerializer import DynamicFieldsModelSerializer
from .models import Role, Permission, RoleHasPermission, AdminUserHasRole, AdminUser
from menus.models import RoleHasMenu, MenuHasPermission, Menu
from menus.serializers import MenuHasPermissionSerializer, MenusInfoSerializer


class RoleListSerializer(DynamicFieldsModelSerializer):
    permission_num = SerializerMethodField()
    permission_list = SerializerMethodField()
    admin_user_num = SerializerMethodField()
    admin_user_list = SerializerMethodField()
    menu_list = SerializerMethodField()

    @staticmethod
    def get_permission_num(obj):
        return RoleHasPermission.objects.filter(flag=1, role_id=obj.id).count()

    @staticmethod
    def get_permission_list(obj):
        return RoleHasPermissionSerializer(RoleHasPermission.objects.filter(flag=1, role_id=obj.id), many=True,
                                           fields=('id', 'permission_info', 'time_create')).data

    @staticmethod
    def get_admin_user_num(obj):
        return AdminUserHasRole.objects.filter(flag=1, role_id=obj.id).count()

    @staticmethod
    def get_admin_user_list(obj):
        return AdminUserHasRoleSerializer(AdminUserHasRole.objects.filter(flag=1, role_id=obj.id), many=True,
                                          fields=('id', 'admin_user_info', 'time_create')).data

    @staticmethod
    def get_menu_list(obj):
        menus_list = MenusInfoSerializer(Menu.objects.filter(show=1, flag=1, before_menu_id__isnull=True).order_by('id'),
                                         many=True, fields=('id', 'child_menu', 'name', 'page_url', 'page_name', 'icon')).data
        if isinstance(obj, list):
            role_menu_id_list = set([item.menu_id for item in RoleHasMenu.objects.filter(role_id__in=obj, flag=1)])
        else:
            role_menu_id_list = [item.menu_id for item in RoleHasMenu.objects.filter(role_id=obj.id, flag=1)]
        main_menu = []
        for item in menus_list:
            if item['id'] in role_menu_id_list:
                if len(item['child_menu']) != 0:
                    child_menu = []
                    for child_item in item['child_menu']:
                        if child_item['id'] in role_menu_id_list:
                            child_menu.append(child_item)
                    item['child_menu'] = child_menu
                main_menu.append(item)
        return main_menu

    class Meta:
        model = Role
        fields = '__all__'


class PermissionSerializer(DynamicFieldsModelSerializer):
    role_list = SerializerMethodField()
    menu_list = SerializerMethodField()

    @staticmethod
    def get_role_list(obj):
        return RoleHasPermissionSerializer(RoleHasPermission.objects.filter(flag=1, permission_id=obj.id), many=True,
                                           fields=('id', 'role_info')).data

    @staticmethod
    def get_menu_list(obj):
        return MenuHasPermissionSerializer(MenuHasPermission.objects.filter(flag=1, permission_id=obj.id), many=True,
                                           fields=('id', 'menu_info')).data

    class Meta:
        model = Permission
        fields = '__all__'


class RoleHasPermissionSerializer(DynamicFieldsModelSerializer):
    permission_info = SerializerMethodField()
    role_info = SerializerMethodField()

    @staticmethod
    def get_permission_info(obj):
        return PermissionSerializer(obj.permission, many=True, fields=('id', 'name', 'codename')).data

    @staticmethod
    def get_role_info(obj):
        return RoleListSerializer(obj.role, fields=('id', 'name', 'codename')).data

    class Meta:
        model = RoleHasPermission
        fields = '__all__'


class AdminUserHasRoleSerializer(DynamicFieldsModelSerializer):
    admin_user_info = SerializerMethodField()

    @staticmethod
    def get_admin_user_info(obj):
        return RoleListSerializer(obj.role, fields=('id', 'name', 'codename', 'tel')).data

    class Meta:
        model = RoleHasPermission
        fields = '__all__'


class AdminUserSerializer(DynamicFieldsModelSerializer):
    user_get_menus = SerializerMethodField()
    user_role = SerializerMethodField()
    user_menu_list = SerializerMethodField()
    user_permission_list = SerializerMethodField()

    def get_user_get_menus(self, obj):
        user_role_list = self.get_user_role(obj)
        user_menus = []
        if user_role_list:
            user_menus = RoleListSerializer([item['admin_user_info']['id'] for item in user_role_list], fields=('menu_list',)).data
        return user_menus

    def get_user_menu_list(self, obj):
        user_role_list = self.get_user_role(obj)
        if user_role_list:
            role_has_menus = RoleHasMenu.objects.filter(menu__flag=1, flag=1, role_id__in=[item['admin_user_info']['id'] for item in user_role_list])
            if role_has_menus:
                menus_list = [item.menu.page_url for item in role_has_menus]
                return menus_list
        return []

    def get_user_permission_list(self, obj):
        user_role_list = self.get_user_role(obj)
        if user_role_list:
            role_has_permission = RoleHasPermission.objects.filter(permission__flag=1, flag=1, role_id__in=[item['admin_user_info']['id'] for item in user_role_list])
            if role_has_permission:
                permission_list = [item.permission.codename for item in role_has_permission]
                return permission_list
        return []

    @staticmethod
    def get_user_role(obj):
        role_list = AdminUserHasRole.objects.filter(Q(time_end__isnull=True) | Q(time_end__gte=timezone.now()),
                                                    Q(time_start__isnull=True) | Q(time_start__lte=timezone.now()),
                                                    flag=1,
                                                    admin_user_id=obj)
        if role_list:
            return AdminUserHasRoleSerializer(role_list, many=True, fields=('admin_user_info',)).data
        else:
            return []

    class Meta:
        model = AdminUser
        fields = '__all__'
