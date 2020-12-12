from django.shortcuts import render, redirect, get_object_or_404
from django.forms import ModelForm

from marcianos.models import nave_nodriza, aeronave, Pasajero

# Naves Nodrizas
class nave_nodrizaForm(ModelForm):
    class Meta:
        model = nave_nodriza
        fields = [
        'nombre',
        ]

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

# Aeronaves
class aeronaveForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(aeronaveForm, self).__init__(*args, **kwargs)
        self.fields['nave_origen'].queryset = nave_nodriza.objects.all()
        self.fields['nave_origen'].label_from_instance = lambda obj: "%s" % (obj.nombre)
        self.fields['nave_destino'].queryset = nave_nodriza.objects.all()
        self.fields['nave_destino'].label_from_instance = lambda obj: "%s" % (obj.nombre)

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

def aeronave_delete(request, pk, template_name='aeronave/borrar_aeronave.html'):
    aero_nave = get_object_or_404(aeronave, pk=pk)
    if request.method=='POST':
        aero_nave.delete()
        return redirect('aeronaves_list')
    return render(request, template_name, {'object': aero_nave})

# Pasajeros

class PasajeroForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super(PasajeroForm, self).__init__(*args, **kwargs)
        self.fields['aeronave_id'].queryset = aeronave.objects.all()
        self.fields['aeronave_id'].label_from_instance = lambda obj: "%s" % (obj.nombre)

    class Meta:
        model = Pasajero
        fields = [
            'nombre',
            'aeronave_id',
        ]


def pasajero_list(request, template_name = 'pasajero/lista.html'):
    pasajeros = Pasajero.objects.all()
    data = {}
    data['object_list'] = pasajeros
    return render(request, template_name, data)

def pasajero_create(request, template_name='pasajero/crear_pasajero.html'):
    form = PasajeroForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('pasajero_list')
    return render(request, template_name, {'form': form})

def pasajero_delete(request, pk, template_name='pasajero/borrar_pasajero.html'):
    pasajero = get_object_or_404(Pasajero, pk=pk)
    if request.method=='POST':
        pasajero.delete()
        return redirect('pasajero_list')
    return render(request, template_name, {'object': pasajero})

def pasajero_update(request, pk, template_name='pasajero/crear_pasajero.html'):
    pasajero = get_object_or_404(Pasajero, pk=pk)
    form = PasajeroForm(request.POST or None, instance=pasajero)
    if form.is_valid():
        form.save()
        return redirect('pasajero_list')
    return render(request, template_name, {'form': form})
