from django.contrib import admin
from .models import Estado, TipoDano, Reporte, Asignacion, Auditoria

@admin.register(Estado)
class EstadoAdmin(admin.ModelAdmin):
    list_display = ['id', 'nombre']

@admin.register(TipoDano)
class TipoDanoAdmin(admin.ModelAdmin):
    list_display = ['id', 'nombre']

@admin.register(Reporte)
class ReporteAdmin(admin.ModelAdmin):
    list_display = ['id', 'titulo', 'estado', 'tipo_dano', 'usuario', 'fecha_creacion']

@admin.register(Asignacion)
class AsignacionAdmin(admin.ModelAdmin):
    list_display = ['id', 'reporte', 'usuario', 'fecha_asignacion']

@admin.register(Auditoria)
class AuditoriaAdmin(admin.ModelAdmin):
    list_display = ['id', 'reporte', 'usuario', 'accion', 'fecha_hora']