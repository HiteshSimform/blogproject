from django.shortcuts import render, redirect, get_list_or_404
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from .forms import CustomUserCreationForm
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .decorators import admin_required, author_required, reader_required
from apps.users.models import CustomUser
from apps.users.forms import LoginUser
from django.http import HttpResponse
# Create your views here.

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # login(request,user)
            return redirect('login-user')
    else:
        form = CustomUserCreationForm()
    return render(request,'users/register.html',{'form':form})

def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password = password)

        if user is not None:
            login(request,user)
            messages.success(request, "Login Successful")
            return redirect(reverse('home'))
        else:
            messages.error(request, "Incorrect username or password")
    form = LoginUser()
    return render(request,'users/login.html',{'form':form})

@login_required
@admin_required
def change_user_role(request,user_id):
    user = get_list_or_404(CustomUser, id = user_id)
    roles = ['admin','author','reader']
    if request.method == 'POST':
        new_role = request.POST.get('role')
        if new_role in roles:
            user.role = new_role
            user.save()
            return redirect('user_list')
        
    return render(request,'users/change_role.html',{'user':user})


def home(request):
    return HttpResponse("Hello")