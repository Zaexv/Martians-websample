from django.shortcuts import render, redirect, get_object_or_404
from django.forms import ModelForm
from django.db.models import CheckConstraint, Q, F

from marcianos.models import nave_nodriza, aeronave, Pasajero, Revision

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


def mostrar_pasajeros(request, pk, template_name = 'pasajero/lista.html'):
    pasajeros = Pasajero.objects.all().filter(aeronave_id=pk)
    data = {}
    data['object_list'] = pasajeros
    return render(request, template_name, data)

def pasajeros_sin_nave(request, pk, template_name = 'pasajero/asignar.html'):
    pasajeros = Pasajero.objects.all().exclude(aeronave_id=pk).filter(aeronave_id=None)
    aero = aeronave.objects.get(pk=pk)
    data = {}
    data['object_list'] = pasajeros
    data['object_aeronave'] = aero
    return render(request, template_name, data)

def asignar_pasajeros(request, pkP, pkA, template_name = 'pasajero/exito.html'):
    pasajero = Pasajero.objects.get(pk=pkP)
    aero = aeronave.objects.get(pk=pkA)
    count_marcianos = Pasajero.objects.all().filter(aeronave_id=pkA).count()
    if count_marcianos >= aero.max_marcianos:
        # No se puede asignar.
        return redirect('error', idError="1",pkP=pkP,pkA=pkA)
    else:
        pasajero.aeronave_id = aero
        pasajero.save()
        return redirect('exito')

def aeronaveList(request, template_name = 'aeronave/lista.html'):
    aeronaves = aeronave.objects.all() #Obtengo la lista de naves
    data = {}
    data['object_list'] = aeronaves #Devuelvo los objetos que voy a pintar
    return render(request, template_name, data)

def aeronave_create(request, template_name = 'aeronave/crear_aeronave.html'):
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
    class Meta:
        model = Pasajero
        fields = [
            'nombre',
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

def error(request, idError, pkP, pkA, template_name='error.html'):
    pasajeros = Pasajero.objects.get(pk = pkP)
    aero = aeronave.objects.get(pk = pkA)
    data = {}
    data['error_type'] = idError
    data['pasajero'] = pasajeros
    data['aeronave'] = aero
    return render(request, template_name, data)

def exito(request, template_name='exito.html'):
    return render(request, template_name, {})

#Revisiones
class RevisionForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(RevisionForm, self).__init__(*args, **kwargs)
        self.fields['aeronave_id'].queryset = aeronave.objects.all()
        self.fields['aeronave_id'].label_from_instance = lambda obj: "%s" % (obj.nombre)
    class Meta:
        model = Revision
        fields = [
            'nombre_revisor',
            'aeronave_id',
            'fecha_revision',
        ]

def revision_list(request, template_name = 'revision/lista.html'):
    revisiones = Revision.objects.all()
    data = {}
    data['object_list'] = revisiones
    return render(request, template_name, data)

def revision_create(request, template_name='revision/crear_revision.html'):
    form = RevisionForm(request.POST or None)
    if form.is_valid():
        aeronave_pk = form['aeronave_id'].value()
        if (Revision.objects.filter(fecha_revision=form['fecha_revision'].value(), aeronave_id__pk = aeronave_pk).count()) > 0:
                return render(request, template_name, {'form': form, 'error': 'Ya existe una revisión con esa fecha'})
        revision = Revision()
        revision.nombre_revisor = form['nombre_revisor'].value()
        revision.aeronave_id = aeronave.objects.get(pk=aeronave_pk)
        revision.fecha_revision = form['fecha_revision'].value()
        revision.num_pasajeros = Pasajero.objects.filter(
                                    aeronave_id__pk=aeronave_pk
                                    ).count()
        revision.save()
        for p in Pasajero.objects.filter(aeronave_id__pk=aeronave_pk):
            revision.pasajeros.add(p)
        revision.save()
        return redirect('revision_list')
    return render(request, template_name, {'form': form})
