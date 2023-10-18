from django.forms import ModelForm
from django.forms import DateInput
from .models import *

class FormVacina(ModelForm):
    class Meta:
        model = Vacina
        fields = ['nome']

class FormAnuncio(ModelForm):
    class Meta:
        model = Anuncio
        fields = ['titulo', 'foto', 'descricao', 'genero', 'peso', 'data_nascimento']
        widgets = {
            'data_nascimento': DateInput(attrs={'type': 'date'})
        }

class FormVacinaAnuncio(ModelForm):
    class Meta:
        model = vacinas_anuncios
        fields = ['vacina', 'data_vacina', 'data_vencimento']
        widgets = {
            'data_vacina': DateInput(attrs={'type': 'date'}),
            'data_vencimento': DateInput(attrs={'type': 'date'}),
        }