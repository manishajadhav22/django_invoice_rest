from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *
from .serializers import *
# Create your views here.


@api_view(['GET'])
def invoicedata(request):
    invoice_obj=Invoice.objects.all()
    serializer=InvoiceSerializer(invoice_obj,many=True)

    return Response({'status':200,'payload':serializer.data})


@api_view(['POST'])
def post_invoicedata(request):
    data=request.data
    serializer=InvoiceSerializer(data=request.data)
    if not serializer.is_valid():
        return Response({'status':403,'message':'something went wrong'})
    serializer.save()
    return Response({'status':200,'payload':data,'message':'you data is saved'})

@api_view(['GET'])
def get_invoicedata(request):
    invoice_detail=InvoiceDetail.objects.all()
    serializer=InvoiceDetailSerializer(invoice_detail,many=True)

    return Response({'status':200,'payload':serializer.data})