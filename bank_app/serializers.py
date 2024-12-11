from rest_framework import serializers
from .models import Bank, Branch

class BankSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bank
        fields = ("id", "name")


class BranchSerializer(serializers.ModelSerializer):
    bank = BankSerializer()  

    class Meta:
        model = Branch
        fields = ("ifsc", "bank", "branch", "address", "city", "district", "state")
