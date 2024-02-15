from django.shortcuts import render, redirect
from django.contrib import messages 
from .models import Ticket
import datetime
from .form import CreateTicketForm, UpdateTicketForm


#view complete ticket details
def view_ticket(request,pk):
    ticket = Ticket.objects.get(pk=pk)
    context = {'ticket' : ticket}
    return render(request, 'ticket/ticket_details.html',context)

"""For Customers"""

#creating a ticket
def create_ticket(request):
    if request.method == 'POST':
        form = CreateTicketForm(request.POST)
        if form.isvalid():
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
        return render(request, 'ticket/create_ticket.html',context)
    
    
    
#update a ticket
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

def all_tickets(request):
    tickets = Ticket.objects.filter(created_by=request.user)
    context = {"tickets" : tickets}
    return render(request, 'ticket/all_tickets.html',context)


#For Staff

#view ticket queue
def ticket_queue(request):
    tickets = Ticket.objects.filter(ticket_status='Pending')
    context = {"tickets":tickets}
    return render(request, 'ticket/ticket_queue.html',context)

# accept a ticket from the queue
def accept_ticket(request,pk):
    ticket = Ticket.objects.get(pk= pk)
    ticket.assigned_to = request.user
    ticket.ticket_status= 'Active'
    ticket.accepted_date = datetime.datetime.now()
    ticket.save()
    messages.info(request,'Ticket has been accepted, Please resolve as soon as possible')
    return redirect('ticket-queue')

#close a ticket
def close_ticket(request,pk):
    ticket = Ticket.objects.get(pk= pk)
    ticket.ticket_status= 'Resolved'
    ticket.closed_date = datetime.datetime.now()
    ticket.is_resolved = True
    ticket.save()
    messages.info(request,'Ticket has been Resolved, Thank you for your great work')
    return redirect('ticket-queue')


#view all the tickets an engineer Working on
def pending_tickets_of_engineer(request):
    tickets = Ticket.objects.filter(assigned_to=request.user,is_resolved=False)
    context = {'tickets': tickets}
    return render(request, 'ticket/pending_tickets_of_engineer.html',context)

#all resolved tickets by an engineer
def resolved_tickets_of_engineer(request):
    tickets = Ticket.objects.filter(assigned_to=request.user,is_resolved=True)
    context = {'tickets': tickets}
    return render(request,'ticket/resolved_tickets_by_engineer.html',context)

    

