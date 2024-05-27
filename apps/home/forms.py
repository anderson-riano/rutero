from django import forms
from .models import Departamento
from apps.authentication.db import execute_query

import json

def readJson(filename):
    with open(filename, 'r') as fp:
        return json.load(fp)

def getDepartamentos():
    departamentos = [('0', 'Seleccione')]
    result = execute_query(('SELECT * ' +
                                    ' FROM departamento c ' +
                                    ' ORDER BY c.nombre '))
    for row in result:
        departamentos.append((row[0], row[1]))

    return departamentos

def getTipoPdv():
    tipos = [('0', 'Seleccione')]
    result = execute_query(('SELECT * ' +
                                    ' FROM tipo_pdv c ' +
                                    ' ORDER BY c.nombre '))
    for row in result:
        tipos.append((row[0], row[1]))

    return tipos

class DepartamentosForm(forms.ModelForm):
    id_departamento = forms.ChoiceField(
                    choices = getDepartamentos(),
                    required = True, label='Departamento',
                    widget=forms.Select(attrs={'class': 'form-control selectpicker', 'id': 'id_departamento',  'name': 'id_departamento', 'data-style': 'btn-success', 'data-live-search': 'true', 'data-parsley-validate': 'true', 'required': ''}),
                    )
    
    id_tipo_pdv = forms.ChoiceField(
                    choices = getTipoPdv(),
                    required = True, label='Tipos',
                    widget=forms.Select(attrs={'class': 'form-control selectpicker', 'id': 'id_tipo_pdv',  'name': 'id_tipo_pdv', 'data-style': 'btn-success', 'data-live-search': 'true', 'data-parsley-validate': 'true', 'required': ''}),
                    )

    class Meta:
            model = Departamento
            fields = ['departamento']

