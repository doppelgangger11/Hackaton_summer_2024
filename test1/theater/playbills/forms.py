from django import forms
from .models import *

class TicketPurchaseForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ['seat_number', 'row_number'] 
