from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('goods/', include('goods.urls')),
    path('users/', include('customer.urls')),
    path('admin/', include('admin_user.urls')),
    path('branch/', include('branch.urls')),
    path('menu/', include('menus.urls')),
    # path('order/', include('order.urls')),
    # path('supplier/', include('supplier.urls'))
]
