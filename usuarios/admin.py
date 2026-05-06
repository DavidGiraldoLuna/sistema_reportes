from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Rol, Usuario

@admin.register(Rol)
class RolAdmin(admin.ModelAdmin):
    list_display = ['id', 'nombre']

@admin.register(Usuario)
class UsuarioAdmin(UserAdmin):
    list_display = ['username', 'email', 'rol', 'activo']
    fieldsets = UserAdmin.fieldsets + (
        ('Información adicional', {'fields': ('rol', 'activo')}),
    )