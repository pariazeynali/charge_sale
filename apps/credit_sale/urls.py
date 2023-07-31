from django.urls import path
from apps.credit_sale.views import seller_list, operation_list, add_credit_to_seller, sell_credit

urlpatterns = [
    path('seller/list', seller_list, name='seller_list'),
    path('operation/list', operation_list, name='operations_log'),
    path('seller/<int:seller_id>/improve-credit/', add_credit_to_seller, name='improve_credit'),
    path('seller/<int:seller_id>/sell-credit/', sell_credit, name='sell_credit'),
]
