from rest_framework import serializers

from apps.credit_sale.models import Seller, Operation


class SellerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Seller
        fields = "__all__"


class OperationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Operation
        exclude = ['operation_time']
