from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages 
from django.contrib.auth.decorators import login_required
from .models import Ticket
import datetime
from .form import CreateTicketForm, UpdateTicketForm, NoteForm


#view complete ticket details
@login_required
def view_ticket(request, pk):
    print(request.user)
    ticket = get_object_or_404(Ticket, pk=pk)
    print(ticket.notes.all())
    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            note = form.save(commit=False)
            note.ticket = ticket
            note.modified_by = request.user
            note.save()
            return redirect('view_ticket', pk=pk)
    else:
        form = NoteForm()
    context = {'ticket': ticket, 'form': form}
    return render(request, 'view_ticket.html', context)

"""For Customers"""

#creating a ticket
@login_required
def create_ticket(request):
    if request.method == 'POST':
        form = CreateTicketForm(request.POST)
        if form.is_valid():
            ticket = form.save(commit=False)
            ticket.created_by = request.user
            ticket.ticket_status = 'Pending'
            ticket.save()
            messages.info(request, 'your ticked has been raised susccefully our staff will be assigned soon')
            return redirect('dashboard')
        else:
            messages.warning(request,"something went wrong, please check the form")
            return redirect('create-ticket')
    else:
        form = CreateTicketForm()
        context= {'form': form}
        return render(request, 'create_ticket.html',context)
    
    
    
#update a ticket
@login_required
def update_ticket(request,pk):
    ticket = Ticket.objects.get(pk=pk)
    if request.method == 'POST':
        form = UpdateTicketForm(request.POST,instance=ticket)
        if form.isvalid():
            form.save()
            messages.info(request, 'your ticked has been Updated all the changed will be stored in the db')
            return redirect('dashboard')
        else:
            messages.warning(request,"something went wrong, please check the form")
            return redirect('update-ticket')
    else:
        form = UpdateTicketForm(instance=ticket)
        context= {'form': form}
        return render(request, 'ticket/update_ticket.html',context)
    
        
            
#viewing all created Tickets
@login_required
def all_tickets(request):
    if request.user.is_customer:
        tickets = Ticket.objects.filter(created_by=request.user)
    else:
        tickets = Ticket.objects.filter(assigned_to=request.user)
    context = {"tickets" : tickets}
    return render(request, 'all_tickets.html',context)


#For Staff

#view ticket queue
@login_required
def ticket_queue(request):
    tickets = Ticket.objects.filter(assigned_to=None)
    context = {"tickets":tickets}
    print(tickets)
    return render(request, 'ticket_queue.html',context)

# accept a ticket from the queue
@login_required
def accept_ticket(request,pk):
    ticket = Ticket.objects.get(pk= pk)
    ticket.assigned_to = request.user
    ticket.ticket_status= 'Active'
    ticket.accepted_date = datetime.datetime.now()
    ticket.save()
    messages.info(request,'Ticket has been accepted, Please resolve as soon as possible')
    return redirect('ticket-queue')

#close a ticket
@login_required
def close_ticket(request,pk):
    ticket = Ticket.objects.get(pk= pk)
    print("ticket is closed")
    ticket.ticket_status= 'Resolved'
    ticket.closed_date = datetime.datetime.now()
    ticket.is_resolved = True
    ticket.save()
    messages.info(request,'Ticket has been Resolved, Thank you for your great work')
    return redirect('ticket-queue')


#view all the tickets an engineer Working on
@login_required
def pending_tickets(request):
    if request.user.is_staff:
        tickets = Ticket.objects.filter(assigned_to=request.user,is_resolved=False)
    else:
        tickets = Ticket.objects.filter(created_by=request.user,is_resolved=False)
    context = {'tickets': tickets}
    print(tickets)
    return render(request, 'pending_tickets.html',context)

#all resolved tickets by an engineer
@login_required
def resolved_tickets_of_engineer(request):
    tickets = Ticket.objects.filter(assigned_to=request.user,is_resolved=True)
    context = {'tickets': tickets}
    return render(request,'resolved_tickets_by_engineer.html',context)


    



