from rest_framework.response import Response
from rest_framework.views import APIView
from globel_config.ListApiView import ListApiView
from rest_framework.pagination import PageNumberPagination
from django_filters.rest_framework import DjangoFilterBackend
from .models import Menu, RoleHasMenu, MenuHasPermission
from .serializers import MenusInfoSerializer
from admin_user.serializers import AdminUserSerializer


class MenuInfoListView(ListApiView):
    pagination_class = PageNumberPagination
    serializer_class = MenusInfoSerializer
    queryset = Menu.objects.filter(flag=1, before_menu_id__isnull=True)
    fields = ['id', 'child_menu', 'role_list', 'permission_list', 'show_state', 'name', 'page_url', 'page_name', 'icon', 'flag']

    def post(self, request, *args, **kwargs):
        resp = {
            'error': 1,
            'msg': '新增失败'
        }
        data = request.data
        data['before_menu'] = data['before_menu'] if 'before_menu' in data and data['before_menu'] != 0 else None
        menu_se = MenusInfoSerializer(data=data)
        menu_se.is_valid()
        if menu_se.errors:
            print(menu_se.errors)
        else:
            menu_se.save()
            resp['error'] = 0
            resp['msg'] = '添加成功'
        return Response(resp)

    def put(self, request, *args, **kwargs):
        resp = {
            'error': 1,
            'msg': '修改失败'
        }
        data = request.data
        permission_name = data['permission_name']
        if permission_name == 'delete_menu':
            menu_del = Menu.objects.filter(flag=1, id=data['menu_id']).update(flag=0)
            menu_role_del = RoleHasMenu.objects.filter(flag=1, menu_id=data['menu_id']).update(flag=0)
            menu_permission_del = MenuHasPermission.objects.filter(flag=1, menu_id=data['menu_id']).update(flag=0 )
            if menu_del and menu_role_del and menu_permission_del:
                resp['error'] = 0
                resp['msg'] = '删除成功'
        if permission_name == 'change_menu_detail':
            menu_data = Menu.objects.filter(flag=1, id=data['menu_id'])
            if menu_data:
                menu_se = MenusInfoSerializer(data=data, partial=True)
                menu_se.is_valid()
                if menu_se.errors:
                    print(menu_se.errors)
                else:
                    menu_se.update(menu_data, menu_se)
                    resp['error'] = 0
                    resp['msg'] = '修改成功'
        return Response(resp)


class UserGetMenuApiView(APIView):
    """
    导航栏菜单
    """
    def get(self, request, *args, **kwargs):
        resp = {
            'error': 1,
            'msg': '获取失败'
        }
        # if 'user_id' in kwargs and kwargs['user_id'] is not None:
        kwargs = {'id': request.query_params['user_id']}
        menu_data = AdminUserSerializer(int(kwargs['id']), fields=('user_get_menus',)).data
        resp['error'] = 0
        resp['msg'] = menu_data
        return Response(resp)

