from django.urls import path
from .views import BranchInfoListView

urlpatterns = [
    path('branchinfo', BranchInfoListView.as_view())
]