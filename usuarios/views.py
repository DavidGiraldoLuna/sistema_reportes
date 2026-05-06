from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Rol, Usuario


def login_view(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            messages.error(request, 'Usuario o contraseña incorrectos.')
    return render(request, 'usuarios/login.html')


def logout_view(request):
    logout(request)
    return redirect('login')


def registro_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        if password1 != password2:
            messages.error(request, 'Las contraseñas no coinciden.')
            return render(request, 'usuarios/registro.html')

        if Usuario.objects.filter(username=username).exists():
            messages.error(request, 'El usuario ya existe.')
            return render(request, 'usuarios/registro.html')

        rol_solicitante = Rol.objects.get(nombre='Solicitante')
        user = Usuario.objects.create_user(
            username=username,
            email=email,
            password=password1,
            rol=rol_solicitante
        )
        messages.success(request, 'Registro exitoso. Inicia sesión.')
        return redirect('login')

    return render(request, 'usuarios/registro.html')


@login_required
def dashboard(request):
    rol = request.user.rol.nombre if request.user.rol else None
    if rol == 'Administrador':
        return redirect('dashboard_admin')
    elif rol == 'Técnico':
        return redirect('dashboard_tecnico')
    else:
        return redirect('dashboard_solicitante')


@login_required
def dashboard_solicitante(request):
    return render(request, 'usuarios/dashboard_solicitante.html')


@login_required
def dashboard_admin(request):
    return render(request, 'usuarios/dashboard_admin.html')


@login_required
def dashboard_tecnico(request):
    return render(request, 'usuarios/dashboard_tecnico.html')