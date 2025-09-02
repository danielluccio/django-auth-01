from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import *
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

def login_user(request):
    if request.method == 'POST':
        form = LoginUserForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect("users:private_page_2")
            else:
                messages.error(request, "Usuário não autenticado !")
                return redirect("users:login_user")
            
    form = LoginUserForm()
    return render(request, 'accounts/login_user.html', {'form': form})


def register_user(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            messages.success(request, "Usuário Registrado com Sucesso !")
            form.save()
            return redirect("users:login_user")
        else:
            messages.error(request, "Usuário não registrado, tente novamente !")
            return redirect("users:register_user")
    form = RegisterForm()
    return render(request, 'accounts/register_user.html', {'form': form})


def logout_user(request):
    logout(request)
    return redirect('users:login_user')

@login_required
def private_page_1(request):
    return render(request, "accounts/private_page_1.html")

@login_required
def private_page_2(request):
    return render(request, "accounts/private_page_2.html")
