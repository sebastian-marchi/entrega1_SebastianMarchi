from django.http import HttpResponse, HttpResponseRedirect, HttpResponseBadRequest
from django.template import loader
from django.shortcuts import render
from familia.forms.forms import AutoForm, BuscarAutosForm

from familia.models.Auto import Auto

def index(request):
    autos = Auto.objects.all()
    template = loader.get_template('familia/lista_familiares.html')
    context = {
        'autos': autos,
    }
    return HttpResponse(template.render(context, request))


def agregar(request):
    '''
    TODO: agregar un mensaje en el template index.html que avise al usuario que 
    la auto fue cargada con éxito
    '''

    if request.method == "POST":
        form = AutoForm(request.POST)
        if form.is_valid():

            marca = form.cleaned_data['marca']
            modelo = form.cleaned_data['modelo']
            anio = form.cleaned_data['anio']
            km = form.cleaned_data['km']
            Auto(marca=marca, modelo=modelo, anio=anio).save()

            return HttpResponseRedirect("/")
    elif request.method == "GET":
        form = AutoForm()
    else:
        return HttpResponseBadRequest("Error no conzco ese metodo para esta request")

    
    return render(request, 'familia/form_carga.html', {'form': form})


def borrar(request, identificador):
    '''
    TODO: agregar un mensaje en el template index.html que avise al usuario que 
    la auto fue eliminada con éxito        
    '''
    if request.method == "GET":
        auto = Auto.objects.filter(id=int(identificador)).first()
        if auto:
            auto.delete()
        return HttpResponseRedirect("/")
    else:
        return HttpResponseBadRequest("Error no conzco ese metodo para esta request")


def actualizar(request, identificador):
    '''
    TODO: implementar una vista para actualización
    '''
    pass


def buscar(request):
    if request.method == "GET":
        form_busqueda = BuscarAutosForm()
        return render(request, 'familia/form_busqueda.html', {"form_busqueda": form_busqueda})

    elif request.method == "POST":
        form_busqueda = BuscarAutosForm(request.POST)
        if form_busqueda.is_valid():
            palabra_a_buscar = form_busqueda.cleaned_data['palabra_a_buscar']
            autos = Auto.objects.filter(marca__icontains=palabra_a_buscar)

        return  render(request, 'familia/lista_familiares.html', {"autos": autos})
    