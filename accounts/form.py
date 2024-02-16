from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class RegisterCustomer(UserCreationForm):
    """
    Form for customer registration, extending the UserCreationForm.
    """

    class Meta:
        """
        Meta class specifying the model and fields for the form.
        """
        model = CustomUser
        fields = ['email', 'username', 'first_name', 'last_name']
