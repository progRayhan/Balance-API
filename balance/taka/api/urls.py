from django.urls import path
from taka.api.views import balance_list, balance_detail

urlpatterns = [
    path('list/', balance_list.as_view(), name='balance-list'),
    path('list/<str:pk>/', balance_detail.as_view(), name='balance-details'),
    
    # path('<int:pk>/balance-create/', BalanceCreate.as_view(), name="balance-create"),
    # path('<int:pk>/balance/', BalanceList.as_view(), name="balance-list"),
    # path('balance/<int:pk>/', BalanceDetail.as_view(), name="balance-detail"),
]