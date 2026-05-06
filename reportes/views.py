from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import ReporteForm
from .models import Reporte, Estado, Asignacion
from usuarios.models import Usuario


@login_required
def crear_reporte(request):
    if request.method == 'POST':
        form = ReporteForm(request.POST, request.FILES)
        if form.is_valid():
            reporte = form.save(commit=False)
            reporte.usuario = request.user
            reporte.estado = Estado.objects.get(nombre='Pendiente')
            reporte.save()
            messages.success(request, 'Reporte enviado correctamente.')
            return redirect('mis_reportes')
    else:
        form = ReporteForm()
    return render(request, 'reportes/crear_reporte.html', {'form': form})


@login_required
def mis_reportes(request):
    reportes = Reporte.objects.filter(usuario=request.user).order_by('-fecha_creacion')
    return render(request, 'reportes/mis_reportes.html', {'reportes': reportes})


@login_required
def lista_reportes_admin(request):
    reportes = Reporte.objects.all().order_by('-fecha_creacion')
    return render(request, 'reportes/lista_reportes_admin.html', {'reportes': reportes})


@login_required
def detalle_reporte_admin(request, reporte_id):
    reporte = get_object_or_404(Reporte, id=reporte_id)
    tecnicos = Usuario.objects.filter(rol__nombre='Técnico')
    return render(request, 'reportes/detalle_reporte_admin.html', {
        'reporte': reporte,
        'tecnicos': tecnicos
    })


@login_required
def validar_reporte(request, reporte_id):
    reporte = get_object_or_404(Reporte, id=reporte_id)
    reporte.estado = Estado.objects.get(nombre='Validado')
    reporte.save()
    return redirect('detalle_reporte_admin', reporte_id=reporte.id)


@login_required
def rechazar_reporte(request, reporte_id):
    if request.method == 'POST':
        motivo = request.POST.get('motivo_rechazo')
        reporte = get_object_or_404(Reporte, id=reporte_id)
        reporte.estado = Estado.objects.get(nombre='Rechazado')
        reporte.motivo_rechazo = motivo
        reporte.save()
    return redirect('lista_reportes_admin')


@login_required
def asignar_tecnico(request, reporte_id):
    if request.method == 'POST':
        tecnico_id = request.POST.get('tecnico_id')
        reporte = get_object_or_404(Reporte, id=reporte_id)
        tecnico = get_object_or_404(Usuario, id=tecnico_id)
        Asignacion.objects.create(reporte=reporte, usuario=tecnico)
        reporte.estado = Estado.objects.get(nombre='Asignado')
        reporte.save()
        messages.success(request, 'Técnico asignado correctamente.')
    return redirect('lista_reportes_admin')


@login_required
def mis_asignaciones(request):
    asignaciones = Asignacion.objects.filter(usuario=request.user).order_by('-fecha_asignacion')
    return render(request, 'reportes/mis_asignaciones.html', {'asignaciones': asignaciones})


@login_required
def atender_reporte(request, reporte_id):
    reporte = get_object_or_404(Reporte, id=reporte_id)
    if request.method == 'POST':
        resultado = request.POST.get('resultado')
        nuevo_estado = request.POST.get('estado')
        reporte.resultado_atencion = resultado
        reporte.estado = Estado.objects.get(nombre=nuevo_estado)
        reporte.save()
        messages.success(request, 'Reporte actualizado correctamente.')
        return redirect('mis_asignaciones')
    return render(request, 'reportes/atender_reporte.html', {'reporte': reporte})

@login_required
def cerrar_reporte(request, reporte_id):
    reporte = get_object_or_404(Reporte, id=reporte_id)
    reporte.estado = Estado.objects.get(nombre='Cerrado')
    from django.utils import timezone
    reporte.fecha_cierre_real = timezone.now()
    reporte.save()
    messages.success(request, 'Reporte cerrado correctamente.')
    return redirect('lista_reportes_admin')