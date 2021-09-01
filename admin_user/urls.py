from django.urls import path
from .views import RoleListView
from .views import PermissionsListView
from .views import AdminUSerLoginApiView
from .views import AdminUserListView


urlpatterns = [
    path('roleinfo', RoleListView.as_view()),
    path('permissioninfo', PermissionsListView.as_view()),
    path('login', AdminUSerLoginApiView.as_view()),
    path('userlist', AdminUserListView.as_view()),
]
