from django import forms


class MotoForm(forms.Form):
    marca = forms.CharField(label="Marca", max_length=100)
    modelo = forms.CharField(label="Modelo", max_length=100)
    tipo = forms.CharField(label ="Tipo", max_length=100)
    anio = forms.IntegerField(label="Año")
    km = forms.IntegerField(label="km")


class BuscarMotosForm(forms.Form):
    palabra_a_buscar = forms.CharField(label="Buscar")
