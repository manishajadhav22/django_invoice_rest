from rest_framework import serializers
from .models import *

class InvoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model=Invoice
        fields="__all__"

class InvoiceDetailSerializer(serializers.ModelSerializer):
    invoice=InvoiceSerializer()
    class Meta:
        model=Invoice
        fields="__all__"
