from rest_framework.views import APIView
from rest_framework.response import Response
from globel_config.ListApiView import ListApiView
from rest_framework.pagination import PageNumberPagination
from django.db.models import Q
from django_filters.rest_framework import DjangoFilterBackend
from .models import Branch, BranchHasAdminUser, BranchHasGoods
from .serializers import BranchInfoSerializers
from .filters import BranchInfoFilter


class BranchInfoListView(ListApiView):
    serializer_class = BranchInfoSerializers
    pagination_class = PageNumberPagination
    queryset = Branch.objects.filter(~Q(flag=0)).order_by('-time_create')
    fields = ['id', 'name', 'address', 'foreman', 'tel', 'time_create', 'branch_has_user']
    filter_backends = (DjangoFilterBackend, )
    filter_class = BranchInfoFilter

    def post(self, request, *args, **kwargs):
        resp = {
            'error': 1,
            'msg': '新增异常'
        }
        data = request.data
        branch_data = Branch.objects.filter(~Q(flag=0), name=data['name'])
        if branch_data:
            resp['msg'] = '门店名称已存在...'
        else:
            branch_data_se = BranchInfoSerializers(data=data)
            branch_data_se.is_valid()
            if branch_data_se.errors:
                resp['msg'] = '参数异常'
            else:
                branch_data_se.save()
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
        if permission_name == 'delete_branch_info':
            branch_del = Branch.objects.filter(flag=1, id=data['id']).update(flag=0)
            branch_user_del = BranchHasAdminUser.objects.filter(flag=1, branch_id=data['id']).update(flag=0)
            if branch_del and branch_user_del:
                resp['error'] = 0
                resp['msg'] = '删除成功'
        if permission_name == 'change_branch_info':
            branch_data = Branch.objects.filter(flag=1, id=data['id'])
            if branch_data:
                branch_se = BranchInfoSerializers(data=data, partial=True)
                branch_se.is_valid()
                if branch_se.errors:
                    print(branch_se.errors)
                else:
                    branch_se.update(branch_data, branch_se)
                    resp['error'] = 0
                    resp['msg'] = '修改成功'
        return Response(resp)