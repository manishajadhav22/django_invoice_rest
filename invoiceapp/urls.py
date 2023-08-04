from django.urls import path
from .views import *
urlpatterns = [
   path('',invoicedata),
   path('invoice/',post_invoicedata),
   path('get_invoicedetail/',get_invoicedata),
]
