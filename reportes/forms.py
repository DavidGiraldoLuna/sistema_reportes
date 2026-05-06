from django import forms
from .models import Reporte, TipoDano


class ReporteForm(forms.ModelForm):
    class Meta:
        model = Reporte
        fields = ['titulo', 'tipo_dano', 'descripcion', 'evidencia']
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Título del reporte'}),
            'tipo_dano': forms.Select(attrs={'class': 'form-select'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'placeholder': 'Describe el daño y la ubicación'}),
            'evidencia': forms.FileInput(attrs={'class': 'form-control'}),
        }
        labels = {
            'titulo': 'Título',
            'tipo_dano': 'Tipo de daño',
            'descripcion': 'Descripción y ubicación',
            'evidencia': 'Fotografía del daño',
        }