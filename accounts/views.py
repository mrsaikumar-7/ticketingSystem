from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .form import RegisterCustomer  # Corrected import statement
from django.contrib.auth.decorators import login_required

# Register User View
def register(request):
    """
    View for user registration.
    """
    if request.method == 'POST':
        form = RegisterCustomer(request.POST)
        if form.is_valid():
            user = form.save(commit=False)  # commit False is because we don't want to save into the db instantly
            # we have to perform some actions and then commit
            user.is_customer = True
            user.save()
            messages.info(request, "Your account has been successfully registered. Please login.")
            return redirect("login")
        else:
            messages.warning(request, "Something went wrong. Please check the form.")
            return redirect('register_user')
    else:
        form = RegisterCustomer()
        context = {'form': form, 'signup_active': True}
        return render(request, 'register_user.html', context=context)


# Login View
def login_user(request):
    """
    View for user login.
    """
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None and user.is_active:
            login(request, user)
            messages.info(request, "Login is successful.")
            return redirect('dashboard')
        else:
            messages.warning(request, "Password and email do not match.")
            return redirect('login')
    else:
        form = RegisterCustomer()
        context = {'form': form, 'signup_active': False}
        return render(request, 'login.html', context)


# Logout View
def logout_user(request):
    """
    View for user logout.
    """
    logout(request)
    messages.info(request, "You are logged out successfully.")
    return redirect('login')


# Profile View
@login_required
def profile(request):
    """
    View for user profile.
    """
    user = request.user
    context = {'user': user}
    return render(request, 'profile.html', context)
