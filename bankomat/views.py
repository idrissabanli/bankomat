from django.shortcuts import render
# from django.views import generic
from rest_framework.views import APIView
from .serializers import CheckSerializer, CashOutSerializer
from django.http import JsonResponse
from .models import  Cart
from rest_framework.exceptions import ValidationError
from rest_framework.authtoken.models import Token


class CheckAPIView(APIView):

    def post(self, request):
        # print(request.data)
        serializer = CheckSerializer(data=request.data)
        if serializer.is_valid(raise_exception=False):
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


# class CashOutAPIView(APIView):
#     def post(self, request):
#         # print(request.data)
#         serializer = CashOutSerializer(data=request.data)
#         if serializer.is_valid(raise_exception=False):
#             print(serializer.data['cart_number'])
#             cart = Cart.objects.filter(cart_number=serializer.data['cart_number'],
#                                        password=serializer.data['password']).first()
#             if not cart:
#                 raise ValidationError({
#                     'detail': "Cart information does not match"
#                 })
#             serializer = CheckSerializer(cart)
#             return JsonResponse(serializer.data, safe=False)
#         return JsonResponse(serializer.errors, safe=False)