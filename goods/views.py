from rest_framework.views import APIView
from rest_framework.response import Response
from globel_config.ListApiView import ListApiView
from rest_framework.pagination import PageNumberPagination
from django.db.models import Q
from django_filters.rest_framework import DjangoFilterBackend
from .models import Goods, GoodsBrand, GoodsCategory, GoodsDiscount, CategoryHasGoods
from .serializers import GoodsInfoSerializers, GoodsBrandSerializers, GoodsCategorySerializers, GoodsDiscountSerializers
from .filters import GoodsInfoFilter


class GoodsInfoListView(ListApiView):
    serializer_class = GoodsInfoSerializers
    pagination_class = PageNumberPagination
    queryset = Goods.objects.filter(~Q(flag=0)).order_by('-time_create')
    fields = ['id', 'uuid', 'name', 'goods_brand', 'goods_category', 'sale_price', 'pic_url', 'flag']
    filter_backends = (DjangoFilterBackend,)
    filter_class = GoodsInfoFilter

    def post(self, request, *args, **kwargs):
        resp = {
            'error': 1,
            'msg': '新增异常'
        }
        data = request.data
        return Response(resp)


class GoodsBrandListView(ListApiView):
    serializer_class = GoodsBrandSerializers
    pagination_class = PageNumberPagination
    queryset = GoodsBrand.objects.filter(~Q(flag=0)).order_by('-time_create')
    fields = ['id', 'name', 'flag']

    def post(self, request, *args, **kwargs):
        resp = {
            'error': 1,
            'msg': '新增异常'
        }
        data = request.data
        brand_data = GoodsBrand.objects.filter(~Q(flag=0), name=data['name'])
        if brand_data:
            resp['msg'] = '品牌名已存在...'
        else:
            brand_data_se = GoodsBrandSerializers(data=data)
            brand_data_se.is_valid()
            if brand_data_se.errors:
                resp['msg'] = '参数异常'
            else:
                brand_data_se.save()
                resp['error'] = 0
                resp['msg'] = '新增成功'
        return Response(resp)

    def put(self, request, *args, **kwargs):
        resp = {
            'error': 1,
            'msg': '修改异常'
        }
        data = request.data
        brand_id_data = GoodsBrand.objects.filter(~Q(flag=0), id=data['id']).first()
        if brand_id_data:
            if 'delete' in data:
                brand_id_data.flag = 0
                brand_id_data.save()
                resp['error'] = 0
                resp['msg'] = '删除成功'
            else:
                brand_data = GoodsBrand.objects.filter(~Q(flag=0), name=data['name'])
                if brand_data:
                    resp['msg'] = '品牌名已存在...'
                else:
                    brand_id_data.name = data['name']
                    brand_id_data.save()
                    resp['error'] = 0
                    resp['msg'] = '修改成功'
        return Response(resp)


class GoodsCategoryListView(ListApiView):
    serializer_class = GoodsCategorySerializers
    pagination_class = PageNumberPagination
    queryset = GoodsCategory.objects.filter(~Q(flag=0)).order_by('-time_create')
    fields = ['id', 'name', 'weight', 'pic_url', 'flag']

    def post(self, request, *args, **kwargs):
        resp = {
            'error': 1,
            'msg': '新增异常'
        }
        data = request.data
        category_data = GoodsCategory.objects.filter(~Q(flag=0), name=data['name'])
        if category_data:
            resp['msg'] = '分类名称已存在...'
        else:
            category_data_se = GoodsCategorySerializers(data=data)
            category_data_se.is_valid()
            if category_data_se.errors:
                resp['msg'] = '参数异常'
            else:
                category_data_se.save()
                resp['error'] = 0
                resp['msg'] = '新增成功'
        return Response(resp)

    def put(self, request, *args, **kwargs):
        resp = {
            'error': 1,
            'msg': '修改异常'
        }
        data = request.data
        category_id_data = GoodsCategory.objects.filter(~Q(flag=0), id=data['id']).first()
        if category_id_data:
            if 'delete' in data:
                category_id_data.flag = 0
                category_id_data.save()
                CategoryHasGoods.objects.filter(flag=1, category_id=data['id']).update(flag=0)
                resp['error'] = 0
                resp['msg'] = '删除成功'
            else:
                category_data = GoodsCategory.objects.filter(~Q(flag=0), name=data['name'])
                if category_data:
                    resp['msg'] = '分类名称已存在...'
                else:
                    category_id_data.name = data['name']
                    category_id_data.save()
                    resp['error'] = 0
                    resp['msg'] = '修改成功'
        return Response(resp)


class GoodsDiscountListView(ListApiView):
    serializer_class = GoodsDiscountSerializers
    pagination_class = PageNumberPagination
    queryset = GoodsDiscount.objects.filter(~Q(flag=0)).order_by('-time_create')
    fields = ['id', 'name', 'value', 'flag']

    def post(self, request, *args, **kwargs):
        resp = {
            'error': 1,
            'msg': '新增异常'
        }
        data = request.data
        discount_data = GoodsDiscount.objects.filter(~Q(flag=0), name=data['name'])
        if discount_data:
            resp['msg'] = '折扣名称已存在...'
        else:
            discount_data_se = GoodsDiscountSerializers(data=data)
            discount_data_se.is_valid()
            if discount_data_se.errors:
                resp['msg'] = '参数异常'
            else:
                discount_data_se.save()
                resp['error'] = 0
                resp['msg'] = '新增成功'
        return Response(resp)

    def put(self, request, *args, **kwargs):
        resp = {
            'error': 1,
            'msg': '修改异常'
        }
        data = request.data
        discount_id_data = GoodsDiscount.objects.filter(~Q(flag=0), id=data['id']).first()
        if discount_id_data:
            if 'delete' in data:
                discount_id_data.flag = 0
                discount_id_data.save()
                # BranchHasGoods.objects.filter(flag=1, discount_id=data['id']).update(flag=0)
                resp['error'] = 0
                resp['msg'] = '删除成功'
            else:
                discount_data = GoodsDiscount.objects.filter(~Q(flag=0), name=data['name'])
                if discount_data:
                    resp['msg'] = '折扣名称已存在...'
                else:
                    discount_id_data.name = data['name']
                    discount_id_data.save()
                    resp['error'] = 0
                    resp['msg'] = '修改成功'
        return Response(resp)
