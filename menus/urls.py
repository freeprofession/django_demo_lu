from django.urls import path
from .views import MenuInfoListView
from .views import UserGetMenuApiView


urlpatterns = [
    path('menuinfo', MenuInfoListView.as_view()),
    path('usermenus', UserGetMenuApiView.as_view())
]