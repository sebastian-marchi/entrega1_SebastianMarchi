from django.http import HttpResponse, HttpResponseRedirect, HttpResponseBadRequest
from django.template import loader
from django.shortcuts import render
from familia.forms.forms_moto import MotoForm, BuscarMotosForm

from familia.models.Moto import Moto

def indexMoto(request):
    motos = Moto.objects.all()
    template = loader.get_template('familia/lista_motos.html')
    context = {
        'motos': motos,
    }
    return HttpResponse(template.render(context, request))


def agregar(request):
    '''
    TODO: agregar un mensaje en el template index.html que avise al usuario que 
    la moto fue cargada con éxito
    '''

    if request.method == "POST":
        form = MotoForm(request.POST)
        if form.is_valid():

            marca = form.cleaned_data['marca']
            modelo = form.cleaned_data['modelo']
            tipo = form.cleaned_data ['tipo']
            anio = form.cleaned_data['anio']
            km = form.cleaned_data['km']
            Moto(marca=marca, modelo=modelo, anio=anio, tipo=tipo).save()

            return HttpResponseRedirect("/moto/")
    elif request.method == "GET":
        formMoto = MotoForm()
    else:
        return HttpResponseBadRequest("Error no conzco ese metodo para esta request")

    
    return render(request, 'familia/form_cargaMoto.html', {'formMoto': formMoto})


def borrar(request, identificador):
    '''
    TODO: agregar un mensaje en el template index.html que avise al usuario que 
    la Moto fue eliminada con éxito        
    '''
    if request.method == "GET":
        moto = Moto.objects.filter(id=int(identificador)).first()
        if moto:
            moto.delete()
        return HttpResponseRedirect("/moto/")
    else:
        return HttpResponseBadRequest("Error no conzco ese metodo para esta request")


def actualizar(request, identificador):
    '''
    TODO: implementar una vista para actualización
    '''
    pass


def buscar(request):
    if request.method == "GET":
        form_busqueda = BuscarMotosForm()
        return render(request, 'familia/form_busqueda.html', {"form_busqueda": form_busqueda})

    elif request.method == "POST":
        form_busqueda = BuscarMotosForm(request.POST)
        if form_busqueda.is_valid():
            palabra_a_buscar = form_busqueda.cleaned_data['palabra_a_buscar']
            motos = Moto.objects.filter(marca__icontains=palabra_a_buscar)

        return  render(request, 'familia/lista_motos.html', {"motos": motos})
    