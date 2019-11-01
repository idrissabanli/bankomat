from django.shortcuts import render
# from django.views import generic
from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView
from .serializers import CheckSerializer, CashOutSerializer
from django.http import JsonResponse
from .models import Cart
from rest_framework.exceptions import ValidationError
from decimal import Decimal



class CheckAPIView(APIView):

    def post(self, request):
        # print(request.data)
        serializer = CheckSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            print(serializer.data['cart_number'])
            cart = Cart.objects.filter(cart_number=serializer.data['cart_number'],
                                       password=serializer.data['password']).first()
            if not cart:
                raise ValidationError({
                    'detail': "Cart information does not match"
                })
            serializer = CheckSerializer(cart)
            return JsonResponse(serializer.data, safe=False)
        return JsonResponse(serializer.errors, safe=False)


class CashOutAPIView(APIView):
    def post(self, request):
        serializer = CashOutSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            cart = Cart.objects.filter(cart_number=serializer.data['cart_number'],
                                       password=serializer.data['password']).first()
            if not cart:
                raise ValidationError({
                    'detail': "Cart information does not match"
                })
            if Decimal(cart.balance) - abs(Decimal(serializer.data['cash'])) < 0:
                raise ValidationError({
                    'detail': "Your account doesn't have enough cash."
                })
            cart.balance = Decimal(cart.balance) - abs(Decimal(serializer.data['cash']))
            cart.save()
            serializer = CheckSerializer(cart)
            return JsonResponse(serializer.data, safe=False)
        return JsonResponse(serializer.errors, safe=False)
