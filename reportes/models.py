from django.db import models
from usuarios.models import Usuario


class Estado(models.Model):
    nombre = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.nombre

    class Meta:
        db_table = 'estado'


class TipoDano(models.Model):
    nombre = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.nombre

    class Meta:
        db_table = 'tipo_dano'


class Reporte(models.Model):
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField(blank=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_cierre_tentativa = models.DateTimeField(null=True, blank=True)
    fecha_cierre_real = models.DateTimeField(null=True, blank=True)
    estado = models.ForeignKey(Estado, on_delete=models.PROTECT)
    tipo_dano = models.ForeignKey(TipoDano, on_delete=models.PROTECT)
    usuario = models.ForeignKey(Usuario, on_delete=models.PROTECT, related_name='reportes')
    evidencia = models.ImageField(upload_to='evidencias/', null=True, blank=True)
    resultado_atencion = models.TextField(null=True, blank=True)
    motivo_rechazo = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.titulo

    class Meta:
        db_table = 'reporte'


class Asignacion(models.Model):
    reporte = models.ForeignKey(Reporte, on_delete=models.CASCADE, related_name='asignaciones')
    usuario = models.ForeignKey(Usuario, on_delete=models.PROTECT, related_name='asignaciones')
    fecha_asignacion = models.DateTimeField(auto_now_add=True)
    fecha_liberacion = models.DateTimeField(null=True, blank=True)
    motivo_reasignacion = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"Asignación {self.reporte} → {self.usuario}"

    class Meta:
        db_table = 'asignacion'


class Auditoria(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.PROTECT, related_name='auditorias')
    reporte = models.ForeignKey(Reporte, on_delete=models.CASCADE, related_name='auditorias')
    accion = models.CharField(max_length=100)
    descripcion = models.TextField(null=True, blank=True)
    fecha_hora = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.accion} - {self.reporte} ({self.fecha_hora})"

    class Meta:
        db_table = 'auditoria'