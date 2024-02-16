from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

def home(request):
    # Check to see if logging in
    if request.method == 'POST':
        username = request.POST['user_name']
        password = request.POST['password']
        # Authenticate
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "You are Logged In")
            return redirect('home')
        else:
            messages.success(request, "There Was an Error Loggin in, Please Try Again.")
            return redirect('home')
        
    return render(request, 'home.html', {})

def logout_user(request):
    logout(request)
    messages.success(request, "You Have Been Logged Out...")
    return redirect('home')