from django.urls import path
from . import views

urlpatterns = [
    path('view-ticket/<int:pk>/', views.view_ticket, name='view_ticket'),
    path('create-ticket', views.create_ticket,name = 'create-ticket'),
    path('update-ticket/<int:pk>/', views.update_ticket, name = 'update-ticket'),
    path('all-tickets', views.all_tickets,name = 'all_tickets'),
    path('ticket-queue/', views.ticket_queue , name = 'ticket-queue'),
    path('accept-ticket/<int:pk>', views.accept_ticket, name= 'accept-ticket'),
    path('close-ticket/<int:pk>' , views.close_ticket, name = 'close-ticket'),
    path('pending-tickets',views.pending_tickets, name = 'pending_tickets_of_engineer'),
    path('resolved-tickets-of-engineer', views.resolved_tickets_of_engineer, name = 'resolved-tickets'),
]
