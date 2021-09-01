from django.urls import path
from .views import GoodsInfoListView
from .views import GoodsBrandListView
from .views import GoodsCategoryListView
from .views import GoodsDiscountListView

urlpatterns = [
    path('goodsinfo', GoodsInfoListView.as_view()),
    path('goodsbrand', GoodsBrandListView.as_view()),
    path('goodscategory', GoodsCategoryListView.as_view()),
    path('goodsdiscount', GoodsDiscountListView.as_view()),
]
