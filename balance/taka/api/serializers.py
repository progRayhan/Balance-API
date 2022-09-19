from dataclasses import fields
from rest_framework import serializers
from taka.models import Balances, Bank

class BalancesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Balances
        fields = '__all__'
        # exclude = ('account_holder',)
        
# class BankSerializer(serializers.ModelSerializer):
#     bank = BalancesSerializer(many=True, read_only=True)
#     class Meta:
#         model = Bank
#         fields = '__all__'