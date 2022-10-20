from .models import Input, Investor, Tender
from rest_framework import serializers


class TenderViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tender
        fields = [
            'id','name','description', 'date_due', 'location', 'contact'
        ]


class InvestViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Investor
        fields = [
            'id', 'name', 'description', 'location', 'contact'
        ]


class InputViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Input
        fields = [
            'id', 'name', 'description', 'quantity', 'contact', 'price'
        ]



