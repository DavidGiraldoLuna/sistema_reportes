from django.urls import path
from . import views

urlpatterns = [
    path('crear/', views.crear_reporte, name='crear_reporte'),
    path('mis-reportes/', views.mis_reportes, name='mis_reportes'),
    path('admin/lista/', views.lista_reportes_admin, name='lista_reportes_admin'),
    path('admin/detalle/<int:reporte_id>/', views.detalle_reporte_admin, name='detalle_reporte_admin'),
    path('admin/validar/<int:reporte_id>/', views.validar_reporte, name='validar_reporte'),
    path('admin/rechazar/<int:reporte_id>/', views.rechazar_reporte, name='rechazar_reporte'),
    path('admin/asignar/<int:reporte_id>/', views.asignar_tecnico, name='asignar_tecnico'),
    path('tecnico/asignaciones/', views.mis_asignaciones, name='mis_asignaciones'),
    path('tecnico/atender/<int:reporte_id>/', views.atender_reporte, name='atender_reporte'),
    path('admin/cerrar/<int:reporte_id>/', views.cerrar_reporte, name='cerrar_reporte'),
]