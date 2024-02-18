from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm, AddRecordForm
from .models import Record

def home(request):
    if request.user.is_authenticated:
        records = Record.objects.all()
        return render(request, 'home.html', {'records': records})
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
            return redirect('login')
    return render(request, 'home.html', {})

def login_user(request):
    return render(request, 'login.html', {})


def logout_user(request):
    logout(request)
    messages.success(request, "You Have Been Logged Out...")
    return redirect('home')

def register_user(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            # Authenticate and login
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, "You have been successfully registered! Welcome!")
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'register.html', {'form': form})

def customer_record(request, pk):
    if request.user.is_authenticated:
        # Look Up Records
        customer_record = Record.objects.get(id=pk)
        return render(request, 'record.html', {'customer_record': customer_record})
    
    messages.success(request, "You must be logged in to view that page.")
    return redirect('home')

def delete_record(request, pk):
    if request.user.is_authenticated:
        # Delete Record
        Record.objects.get(id=pk).delete()
        messages.success(request, f"ID-{pk} Record Deleted Success!")
        return redirect('home')
    
    messages.success(request, "You must be logged in to delete records.")
    return redirect('home')

def add_record(request):
    if request.user.is_authenticated:
        form = AddRecordForm(request.POST or None)
        if request.method == "POST":
            if form.is_valid():
                add_record = form.save()
                messages.success(request, "Record Added Success!")
                return redirect('home')
        return render(request, 'add_record.html',  {'form': form})
    
    messages.success(request, "You must be logged in to add records.")
    return redirect('home')

def update_record(request, pk):
    if request.user.is_authenticated:
        current_record = Record.objects.get(id=pk)
        form = AddRecordForm(request.POST or None, instance=current_record)
        if form.is_valid():
            form.save()
            messages.success(request, f"ID-{pk} Record has been updated!")
            return redirect('home')
        return render(request, 'update_record.html', {'form':form})
    
    messages.success(request, "You must be logged in to update records.")
    return redirect('home')