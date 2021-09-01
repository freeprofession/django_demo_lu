from django.shortcuts import HttpResponse
from django.utils.deprecation import MiddlewareMixin
import json
from admin_user.serializers import AdminUserSerializer


class RequestMiddlewareMixin(MiddlewareMixin):

    def process_view(self, request, *args, **kwargs):
        kwargs['user_id'] = request.META.get("HTTP_USERID") or ''
        method_dict = dict()
        for k, v in request.query_params.items():
            method_dict[k] = v
        for k, v in request.data.items():
            method_dict[k] = v
        if 'page_name' not in method_dict.keys() or 'permissions_name' not in method_dict.keys():
            return HttpResponse(json.dumps({
                'error': -10001,
                'msg': '验证参数检测失败'
            }))
        # 检测页面权限是否可用
        page_name = method_dict['page_name']
        permissions_name = method_dict['permissions_name']
        user_page_permission_list = AdminUserSerializer(kwargs['user_id'], fields=('user_menu_list', 'user_permission_list')).data
        if page_name not in user_page_permission_list['user_menu_list']:
            return HttpResponse(json.dumps({
                'error': -10002,
                'msg': '权限检测失败'
            }))
        if permissions_name not in user_page_permission_list['user_permission_list']:
            return HttpResponse(json.dumps({
                'error': -10003,
                'msg': '操作权限异常'
            }))

