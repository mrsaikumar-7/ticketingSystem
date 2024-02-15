from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth import authenticate , login,logout
from .form import RegisterCustomer


# Create your views here.

def register(request):
    if request.method == 'POST':
        form = RegisterCustomer(request.POST)
        if form.is_valid():
            user = form.save(commit=False) #commit False is because we dont want to save into db instantly 
            #we have to perform some actions and then commit
            print(user)
            user.is_customer = True
            user.save()
            messages.info(request, "Your account has been succesfully registered, Please login")
            return redirect("login")
        else:
            print(form)
            messages.warning(request,"Something went wrong please check the form")
            return redirect('register_user')
    else:
        form = RegisterCustomer()
        context = {'form':form,'signup_active': True}
        return render(request,'register_user.html',context= context)
    

#login 
def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username= username,password = password)
        if user is not None and user.is_active:
            login(request,user)
            messages.info(request,"login is successful")
            return redirect('dashboard')
        else:
            messages.warning(request, "Password and email not matched")
            return redirect('login')
    else:
        form = RegisterCustomer()
        context = {'form':form,'signup_active': False}
        return render(request,'login.html', context)
    
        
#logout
def logout_user(request):
    logout(request)
    messages.info(request, "You are logged out succesfully")
    return redirect('login')
            