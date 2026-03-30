from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
from .forms import UserRegisterForm, UserUpdateForm


def user_index(request):
    if request.user.is_authenticated:
        return redirect('user:profile')
    return render(request, ... )


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, f"Conta criada com sucesso para {user.username}!")
            return redirect('tarefas:task_list')
    else:
        form = UserRegisterForm()
    return render(request, 'user/register.html', {'form': form})


@login_required
def profile(request):
    return render(request, 'user/profile.html')

@login_required
def profile_update(request):
    if request.method == 'POST':
        form = UserUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, "Seu perfil foi atualizado!")
            return redirect('user:profile')
    else:
        form = UserUpdateForm(instance=request.user)
    return render(request, 'user/profile_form.html', {'form': form})

@login_required
def account_delete(request):
    if request.method == 'POST':
        user = request.user
        logout(request)
        user.delete()
        messages.success(request, "Sua conta foi excluída com sucesso.")
        return redirect('user:user_index')