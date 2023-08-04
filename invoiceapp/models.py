from django.db import models

# Create your models here.
class Invoice(models.Model):
    dt=models.DateField()
    invoice_no=models.IntegerField(max_length=100)
    cust_name=models.CharField(max_length=100)
    
class InvoiceDetail(models.Model):
   invoice=models.ForeignKey(Invoice,on_delete=models.CASCADE)
   desc=models.TextField()
   quant=models.IntegerField(max_length=100)
   unit_price=models.FloatField(max_length=100)
   price=models.FloatField(max_length=100)