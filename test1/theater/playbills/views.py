from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import *

def buy_ticket(request, playbill_id):
    playbill = Playbill.objects.get(id=playbill_id)
    if request.method == 'POST':
        form = TicketPurchaseForm(request.POST)
        if form.is_valid():
            ticket = form.save(commit=False)
            ticket.user = request.user
            ticket.playbill = playbill
            ticket.save()
            return redirect('confirm_purchase', ticket_id=ticket.id)
    else:
        form = TicketPurchaseForm()
    return render(request, 'playbills/buy_ticket.html', {'form': form, 'playbill': playbill})

def confirm_purchase(request, ticket_id):
    ticket = Ticket.objects.get(id=ticket_id)
    return render(request, 'playbills/confirm_purchase.html', {'ticket': ticket})



def playbill_list(request):
    playbills = Playbill.objects.all()
    return render(request, 'playbills/playbill_list.html', {'playbills': playbills})

