from django import forms
from .models import Alergia, Usuario, Vacina, Agenda


class AlergiaForm(forms.ModelForm):
    class Meta:
        model = Alergia
        fields = '__all__'


class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = '__all__'


class VacinaForm(forms.ModelForm):
    class Meta:
        model = Vacina
        fields = '__all__'


class AgendaForm(forms.ModelForm):
    class Meta:
        model = Agenda
        exclude = ['situacao', 'data_situacao', 'dose_vacina']

