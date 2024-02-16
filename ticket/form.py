from .models import Note
from django import forms
from .models import Ticket

class CreateTicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ['title','description']
        
class UpdateTicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ['title','description']
        
class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ['note'] 
        