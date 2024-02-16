from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from ticket.models import Ticket

@login_required
def dashboard(request):
    # Retrieve the count of each ticket status
    if request.user.is_staff:
        total_tickets = Ticket.objects.filter(assigned_to=request.user).count()
        active_tickets = Ticket.objects.filter(ticket_status='Active' , assigned_to = request.user).count()
        pending_tickets = Ticket.objects.filter(ticket_status='Pending' , assigned_to=request.user).count()
        resolved_tickets = Ticket.objects.filter(ticket_status='Resolved',assigned_to=request.user).count()
    else:
        total_tickets = Ticket.objects.filter(created_by=request.user).count()
        active_tickets = Ticket.objects.filter(ticket_status='Active' , created_by = request.user).count()
        pending_tickets = Ticket.objects.filter(ticket_status='Pending' , created_by=request.user).count()
        resolved_tickets = Ticket.objects.filter(ticket_status='Resolved',created_by=request.user).count()
    # Create context dictionary
    context = {
        'totalTickets': total_tickets,
        'activeTickets': active_tickets,
        'pendingTickets': pending_tickets,
        'resolvedTickets': resolved_tickets,
    }

    # Pass the context to the template
    return render(request, 'dashboard.html', context)
