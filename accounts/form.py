from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class RegisterCustomer(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['email','username']
        
