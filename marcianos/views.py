from django.shortcuts import render, redirect, get_object_or_404
from django.forms import ModelForm

from marcianos.models import nave_nodriza, aeronave

# Naves Nodrizas
class nave_nodrizaForm(ModelForm):
    class Meta:
        model = nave_nodriza
        fields = ['nombre']

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

#Aeronaves
class aeronaveForm(ModelForm):
    class Meta:
        model = aeronave
        fields = [
         'nombre',
         'max_marcianos',
         'nave_origen',
         'nave_destino'
         ]

def aeronaveList(request, template_name = 'aeronave/lista.html'):
    aeronaves = aeronave.objects.all() #Obtengo la lista de naves
    data = {}
    data['object_list'] = aeronaves #Devuelvo los objetos que voy a pintar
    return render(request, template_name, data)

def aeronave_create(request, template_name='aeronave/crear_aeronave.html'):
    form = aeronaveForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('aeronaves_list')
    return render(request, template_name, {'form': form})
