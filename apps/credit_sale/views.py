from django.shortcuts import get_object_or_404
from django.db import transaction
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from apps.credit_sale.serializers import SellerSerializer, OperationSerializer
from apps.credit_sale.models import Seller, Operation


@api_view(['GET', 'POST'])
def seller_list(request):
    if request.method == 'GET':
        sellers = Seller.objects.all()
        serializer = SellerSerializer(sellers, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = SellerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def operation_list(request):
    operations = Operation.objects.all()
    serializer = OperationSerializer(operations, many=True)
    return Response(serializer.data)


@transaction.atomic()
@api_view(['POST'])
def add_credit_to_seller(request, seller_id):
    seller = get_object_or_404(Seller, pk=seller_id)

    credit_value = request.data.get('credit')
    seller.credit += credit_value
    seller.save()

    operation = {
        'seller': seller_id,
        'operation': 1
    }
    operation_serializer = OperationSerializer(data=operation)
    if operation_serializer.is_valid():
        operation_serializer.save()
        return Response({'message': 'Seller credit increased successfully'})
    return Response(operation_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@transaction.atomic()
@api_view(['POST'])
def sell_credit(request, seller_id):
    data = request.data
    seller = get_object_or_404(Seller, pk=seller_id)

    credit_value = data.get('credit_value')
    if credit_value > seller.credit:
        return Response({'error': 'Insufficient credit'}, status=status.HTTP_400_BAD_REQUEST)

    seller.credit -= credit_value
    seller.save()

    operation = {
        'seller': seller_id,
        'phone_number': data.get('phone_number'),
        'operation': 0
    }
    operation_serializer = OperationSerializer(data=operation)
    if operation_serializer.is_valid():
        operation_serializer.save()
        return Response({'message': 'Phone_number credit increased successfully'})
    return Response(operation_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
