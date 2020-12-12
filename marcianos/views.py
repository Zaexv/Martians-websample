from django.shortcuts import render, redirect, get_object_or_404
from django.forms import ModelForm

from marcianos.models import nave_nodriza, aeronave, Pasajero

# Create your views here.
class nave_nodrizaForm(ModelForm):
    class Meta:
        model = nave_nodriza
        fields = ['nombre']

class aeronaveForm(ModelForm):
    class Meta:
        model = aeronave
        fields = ['nombre', 'max_marcianos', 'nave_origen', 'nave_destino']

class PasajeroForm(ModelForm):
    class Meta:
        model = Pasajero
        fields = ['nombre', 'aeronave_id']


def nave_nodrizaList(request, template_name = 'nave_nodriza/lista.html'):
    naves_nodrizas = nave_nodriza.objects.all() #Obtengo la lista de naves
    data = {}
    data['object_list'] = naves_nodrizas #Devuelvo los objetos que voy a pintar
    return render(request, template_name, data)


def nave_nodriza_create(request, template_name='nave_nodriza/crear_nave.html'):
    form = nave_nodrizaForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('naves_list')
    return render(request, template_name, {'form': form})

def nave_nodriza_delete(request, pk, template_name='nave_nodriza/borrar_nave.html'):
    nave = get_object_or_404(nave_nodriza, pk=pk)
    if request.method=='POST':
        nave.delete()
        return redirect('naves_list')
    return render(request, template_name, {'object': nave})

def pasajero_list(request, template_name = 'pasajero/lista_pasajeros.html'):
    pasajeros = Pasajero.objects.all()
    data = {}
    data['object_list'] = pasajeros
    return render(request, template_name, data)


def pasajero_create(request, template_name='nave_nodriza/crear_pasajero.html'):
    form = PasajeroForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('pasajeros_list')
    return render(request, template_name, {'form': form})
