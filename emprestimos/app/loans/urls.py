from django.urls import path
from .views import *

urlpatterns = [
    path('customer-loans', LoansView.as_view(), name='customer-loans'),
]