from django.urls import path
from .views import CustomerInfoListView
from .views import CustomerWalletListView
from .views import CustomerWalletHistoryListView


urlpatterns = [
    path('userinfo', CustomerInfoListView.as_view()),
    path('userwallet', CustomerWalletListView.as_view()),
    path('userwallethistory', CustomerWalletHistoryListView.as_view())
]
