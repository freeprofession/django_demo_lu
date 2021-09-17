from rest_framework.views import APIView
from rest_framework.response import Response
from globel_config.ListApiView import ListApiView
from rest_framework.pagination import PageNumberPagination
from django_filters.rest_framework import DjangoFilterBackend
from django.db.models import Q
from .utils import password_to_md
from .models import Role, Permission, RoleHasPermission, AdminUser, AdminUserRecord
from menus.models import MenuHasPermission
from .serializers import RoleListSerializer, PermissionSerializer, AdminUserSerializer


class RoleListView(ListApiView):
    queryset = Role.objects.filter(~Q(flag=0)).order_by('time_create')
    serializer_class = RoleListSerializer
    fields = ['id', 'name', 'codename', 'flag', 'time_create', 'permission_num', 'permission_list', 'admin_user_num', 'admin_user_list', 'menu_list']

    def post(self, request, *args, **kwargs):
        resp = {
            'error': 1,
            'msg': '新增失败'
        }
        data = request.data
        role_data = Role.objects.filter(~Q(flag=0))
        role_data_se = RoleListSerializer(data=data)
        role_data_se.is_valid()
        if role_data_se.errors:
            resp['msg'] = '参数异常'
        else:
            for item in role_data:
                if item.name == data['name'] or item.codename == data['codename']:
                    resp['msg'] = '角色已存在...'
                    return Response(resp)
            role_data_se.save()
            resp['error'] = 0
            resp['msg'] = '新增成功'
        return Response(resp)

    def put(self, request, *args, **kwargs):
        resp = {
            'error': 1,
            'msg': '修改失败'
        }
        data = request.data
        role_data = Role.objects.filter(~Q(flag=0), id=data['id'] if 'id' in data else '')
        if role_data:
            if Role.objects.filter(~Q(flag=0),
                                   Q(codename=data['codename'] if 'codename' in data else '') |
                                   Q(name=data['name'] if 'name' in data else '')):
                resp['msg'] = '角色名或校验名重复'
            else:
                RoleListSerializer().update(role_data, data)
                resp['error'] = 0
                resp['msg'] = '资料修改成功'
        return Response(resp)


class PermissionsListView(ListApiView):
    serializer_class = PermissionSerializer
    pagination_class = PageNumberPagination
    fields = ['id', 'name', 'codename', 'flag', 'time_create', 'role_list', 'menu_list']
    filter_backends = (DjangoFilterBackend,)

    def get_queryset(self):
        if 'name' in self.request.query_params:
            name = self.request.query_params['name']
            return Permission.objects.filter(~Q(flag=0), Q(name=name) | Q(codename=name)).order_by('-time_create')
        return Permission.objects.filter(~Q(flag=0)).order_by('-time_create')

    def post(self, request, *args, **kwargs):
        resp = {
            'error': 1,
            'msg': '新增失败'
        }
        data = request.data
        permission_data = Permission.objects.filter(~Q(flag=0))
        for item in permission_data:
            if item.name == data['name'] or item.codename == data['codename']:
                resp['msg'] = '权限名已存在...'
                return Response(resp)
        permission_data_se = RoleListSerializer(data=data)
        permission_data_se.is_valid()
        if permission_data_se.errors:
            resp['msg'] = '参数异常'
        else:
            permission_data_se.save()
            resp['error'] = 0
            resp['msg'] = '新增成功'
        return Response(resp)

    def put(self, request, *args, **kwargs):
        resp = {
            'error': 1,
            'msg': '修改失败'
        }
        data = request.data
        permission_name = data['permission_name']
        if permission_name == 'delete_permission':
            permission_del = Permission.objects.filter(flag=1, id=data['id']).update(flag=0)
            role_permission_del = RoleHasPermission.objects.filter(flag=1, permission_id=data['id']).update(flag=0)
            menu_permission_del = MenuHasPermission.objects.filter(flag=1, menu_id=data['menu_id']).update(flag=0)
            if permission_del and role_permission_del and menu_permission_del:
                resp['error'] = 0
                resp['msg'] = '删除成功'
        elif permission_name == 'change_permission_msg':
            permission_data = Permission.objects.filter(~Q(flag=0), id=data['id'] if 'id' in data else '')
            if permission_data:
                if Permission.objects.filter(~Q(flag=0),
                                             Q(codename=data['codename'] if 'codename' in data else '') |
                                             Q(name=data['name'] if 'name' in data else '')):
                    resp['msg'] = '权限名或校验名重复'
                else:
                    PermissionSerializer().update(permission_data, data)
                    resp['error'] = 0
                    resp['msg'] = '资料修改成功'
        return Response(resp)


class AdminUSerLoginApiView(APIView):

    def get(self, request, *args, **kwargs):
        resp = {
            'error': 1,
            'msg': '参数错误'
        }
        data = request.query_params
        user_id = data['user_id'] if 'user_id' in data else None
        token = data['token'] if 'token' in data else None
        return Response(resp)

    def post(self, request, *args, **kwargs):
        resp = {
            'error': 1,
            'msg': '参数错误'
        }
        data = request.data
        username = data['username'] if 'username' in data else None
        password = data['password'] if 'password' in data else None
        if username and password:
            user = AdminUser.objects.filter(flag=1, is_available=1, username=username, password=password_to_md(password)).first()
            if user:
                user.is_login = 1
                user.save()
                AdminUserRecord.objects.create({'admin_user_id': user.id, 'type': 'login'})
                resp['error'] = 0,
                resp['msg'] = {
                    'id': user.id,
                    'name': user.name
                }
            else:
                resp['msg'] = '账户失效'
        else:
            resp['msg'] = '用户名或密码错误'
        return Response(resp)


class AdminUserListView(ListApiView):
    serializer_class = AdminUserSerializer
    pagination_class = PageNumberPagination
    queryset = AdminUser.objects.filter(flag=1).order_by('-time_create')
    fields = ['id', 'name', 'username', 'is_available', 'time_create', 'is_login', 'tel', 'user_get_menus']
    filter_backends = (DjangoFilterBackend,)
