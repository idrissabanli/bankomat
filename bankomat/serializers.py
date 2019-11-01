from django.core.validators import MaxValueValidator, MinValueValidator, MinLengthValidator
from rest_framework import serializers
from .models import Cart


class CheckSerializer(serializers.ModelSerializer):
    balance = serializers.DecimalField(read_only=True, max_digits=6, decimal_places=2)
    full_name = serializers.CharField(read_only=True, max_length=40)

    class Meta:
        model = Cart
        fields = [
            'cart_number',
            'password',
            'balance',
            'full_name',
        ]


class CashOutSerializer(serializers.ModelSerializer):
    cash = serializers.DecimalField(max_digits=6, decimal_places=2)

    class Meta:
        model = Cart
        fields = [
            'cart_number',
            'password',
            'cash',
        ]
