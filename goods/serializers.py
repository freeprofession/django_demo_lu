from rest_framework.serializers import SerializerMethodField
from globel_config.DynamicFieldsModelSerializer import DynamicFieldsModelSerializer
from .models import Goods, CategoryHasGoods, GoodsBrand, GoodsCategory, GoodsDiscount


class GoodsInfoSerializers(DynamicFieldsModelSerializer):
    goods_brand = SerializerMethodField()
    goods_category = SerializerMethodField()

    @staticmethod
    def get_goods_brand(obj):
        return {
            'id': obj.brand.id,
            'name': obj.brand.name
        }

    @staticmethod
    def get_goods_category(obj):
        category_data = CategoryHasGoods.objects.filter(flag=1, goods_id=obj.id)
        return [{'id': item.category.id, 'name': item.category.name} for item in category_data]

    class Meta:
        model = Goods
        fields = '__all__'


class GoodsBrandSerializers(DynamicFieldsModelSerializer):

    class Meta:
        model = GoodsBrand
        fields = '__all__'


class GoodsCategorySerializers(DynamicFieldsModelSerializer):

    class Meta:
        model = GoodsCategory
        fields = '__all__'


class GoodsDiscountSerializers(DynamicFieldsModelSerializer):

    class Meta:
        model = GoodsDiscount
        fields = '__all__'
